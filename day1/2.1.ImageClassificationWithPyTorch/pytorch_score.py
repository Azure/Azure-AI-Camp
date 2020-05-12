# Licensed under the MIT license.

import os
import torch
import torch.nn as nn
from torchvision import transforms
import json
from PIL import Image
import numpy as np

from azureml.core.model import Model


def transform_image(array):
    """Transform a numpy array into a torch tensor, 
    resized and normalized correctly - most torchvision
    transforms operate on PIL Image format"""
    # Prepare image for inference
    loader = transforms.Compose([
            transforms.Resize(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    # Converts to a PIL Image
    image = Image.fromarray(np.uint8(array))
    # Creates a torch tensor
    image = loader(image).float()
    # Add a dimension to beginning of tensor ("batch")
    image = image.unsqueeze(0)
    return image

def init():
    global model
    # Get a registered model
    model_path = Model.get_model_path('suspicious-behavior-pytorch')
    # Load with pytorch
    model = torch.load(model_path, map_location=lambda storage, loc: storage)
    # Set to evaluation mode
    model.eval()

def run(input_data):
#     input_data = torch.tensor(np.array(json.loads(input_data)['data']))
    input_data = transform_image(np.array(json.loads(input_data)['data']))

    classes = ['normal', 'suspicious']

    # get prediction
    with torch.no_grad():

        output = model(input_data)
        softmax = nn.Softmax(dim=1)
        pred_probs = softmax(output).numpy()[0]
        index = torch.argmax(output, 1)

    result = {"label": classes[index], "probability": str(pred_probs[index])}
    return result