"""
Based on:  https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
In this tutorial, you will learn how to train your network using
transfer learning. You can read more about the transfer learning at `cs231n
notes <http://cs231n.github.io/transfer-learning/>`__
Quoting these notes,
    In practice, very few people train an entire Convolutional Network
    from scratch (with random initialization), because it is relatively
    rare to have a dataset of sufficient size. Instead, it is common to
    pretrain a ConvNet on a very large dataset (e.g. ImageNet, which
    contains 1.2 million images with 1000 categories), and then use the
    ConvNet either as an initialization or a fixed feature extractor for
    the task of interest.
These two major transfer learning scenarios look as follows:
-  **Finetuning the convnet**: Instead of random initializaion, we
   initialize the network with a pretrained network, like the one that is
   trained on imagenet 1000 dataset. Rest of the training looks as
   usual.
-  **ConvNet as fixed feature extractor**: Here, we will freeze the weights
   for all of the network except that of the final fully connected
   layer. This last fully connected layer is replaced with a new one
   with random weights and only this layer is trained.
**Original Author**: `Sasank Chilamkurthy <https://chsasank.github.io>`_
"""

from __future__ import print_function, division
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
from torchvision import datasets, models, transforms
import numpy as np
import time
import os
import copy
import argparse
import zipfile


from azureml.core.run import Run
from azureml.core import Datastore

# get the Azure ML run object
run = Run.get_context()

def load_data():
    """Load the train/val data."""

    # Data augmentation and normalization for training
    # Just normalization for validation
    data_transforms = {
        'train': transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
        'val': transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),
    }

    image_datasets = {x: datasets.ImageFolder(os.path.join('data', x),
                                              data_transforms[x])
                      for x in ['train', 'val']}
    dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=100,
                                                  shuffle=True, num_workers=0)
                   for x in ['train', 'val']}
    dataset_sizes = {x: len(image_datasets[x]) for x in ['train', 'val']}
    class_names = image_datasets['train'].classes

    return dataloaders, dataset_sizes, class_names


def train_model(model, criterion, optimizer, scheduler, num_epochs, data_dir):
    """Train the model."""
    
    # Unpack the data in data_dir (which is a zipped directory)
    with zipfile.ZipFile(data_dir, 'r') as zip_ref:
        # This should result in a folder called "data"
        zip_ref.extractall('.')
    
    # load training/validation data
    dataloaders, dataset_sizes, class_names = load_data()

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0

    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        # Each epoch has a training and validation phase
        for phase in ['train', 'val']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()   # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = criterion(outputs, labels)

                # backward + optimize only if in training phase
                if phase == 'train':
                    loss.backward()
                    optimizer.step()
                    

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(
                phase, epoch_loss, epoch_acc))

            # deep copy the model
            if phase == 'val' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())

            # log the best val accuracy and the epoch loss to AML run
            if phase == 'train':
                run.log('best_val_acc', np.float(best_acc))
                run.log('epoch_loss', np.float(epoch_loss))

        scheduler.step()

        print()

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(
        time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model

def freeze_layers(model, stop_layer):
    """Utility to stop tracking gradients in earlier layers of
    NN for transfer learning.  Skip batch norm layers."""
    cntr = 1
    for name, param in model.named_parameters():
        if cntr < stop_layer:
            param.requires_grad = False
        else:
            if 'batch_norm' not in name:
                print("Parameter has gradients tracked.")
                param.requires_grad = True
            else:
                param.requires_grad = False
        cntr+=1
        return model

def fine_tune_model(num_epochs, data_dir, learning_rate, momentum, transfer_learn):
    """Load a pretrained model and modify the final fully connected layer.
    More info at: https://pytorch.org/tutorials/beginner/finetuning_torchvision_models_tutorial.html
    """

    # log the hyperparameter metrics to the AML run
    run.log('lr', np.float(learning_rate))
    run.log('momentum', np.float(momentum))

    ## Resnet18 with 2 classes
    # model_ft = models.resnet18(pretrained=transfer_learn)
    # num_ftrs = model_ft.fc.in_features
    # model_ft.fc = nn.Linear(num_ftrs, 2)  # only 2 classes to predict

    # Sqeezenet with 2 classes
    model_ft = models.squeezenet1_0(pretrained=transfer_learn)
    model_ft.classifier[1] = nn.Conv2d(512, 2, kernel_size=(1,1), stride=(1,1))
    model_ft.num_classes = 2

    # Freeze all layers but certain number of last layers
    model_ft = freeze_layers(model_ft, 10)

    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    model_ft = model_ft.to(device)

    criterion = nn.CrossEntropyLoss()

    # Observe that all parameters are being optimized
    optimizer_ft = optim.SGD(model_ft.parameters(),
                             lr=learning_rate, momentum=momentum)

    # Decay LR by a factor of 0.1 every 7 epochs
    exp_lr_scheduler = lr_scheduler.StepLR(
        optimizer_ft, step_size=7, gamma=0.1)

    model = train_model(model_ft, criterion, optimizer_ft,
                        exp_lr_scheduler, num_epochs, data_dir)

    # Complete the run
    run.complete()

    return model

def main():
    print("PyTorch version:", torch.__version__)

    # get command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str, help='data directory',
                        default='data')
    parser.add_argument('--num_epochs', type=int, default=25,
                        help='number of epochs to train')
    parser.add_argument('--output_dir', type=str, help='output directory',
                        default='models')
    parser.add_argument('--learning_rate', type=float,
                        default=0.001, help='learning rate')
    parser.add_argument('--trans', type=str, default='True',
                        help='Set to True if wishing to use transfer learning')
    parser.add_argument('--momentum', type=float, default=0.9, help='momentum')
    args = parser.parse_args()

    print("data directory is: {}".format(args.data_dir))
    print("using transfer learning: {}".format(args.trans))
    model = fine_tune_model(args.num_epochs, args.data_dir,
                            args.learning_rate, args.momentum, bool(args.trans))
    os.makedirs(args.output_dir, exist_ok=True)
    torch.save(model, os.path.join(args.output_dir, 'model_finetuned.pth'))
    # model = run.register_model(model_name='suspicious-behavior-pytorch', 
    #     model_path=os.path.join(args.output_dir, 'model_finetuned.pth'))

if __name__ == "__main__":
    main()
