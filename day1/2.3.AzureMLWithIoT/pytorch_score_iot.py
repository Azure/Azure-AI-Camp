# Licensed under the MIT license.

import os
import torch
import torch.nn as nn
from torchvision import transforms
import json
from PIL import Image
import numpy as np
import base64
from io import BytesIO

from azureml.core.model import Model


def transform_image(input_data):
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
    image = Image.open(BytesIO(input_data))
    # Creates a torch tensor
    image = loader(image).float()
    # Add a dimension to beginning of tensor ("batch")
    image = image.unsqueeze(0)
    return image

def init():
    global model
    # Get a registered model
    AZUREML_MODEL_DIR = os.getenv('AZUREML_MODEL_DIR', '') # this env var is native to the Azure ML container
    model_path = os.path.join(AZUREML_MODEL_DIR, 'model_finetuned.pth')
    # Load with pytorch
    model = torch.load(model_path, map_location=lambda storage, loc: storage)
    # Set to evaluation mode
    model.eval()

def run(input_data):
    # Load IoT video simulator message with base64 encoded image
    input_json = json.loads(input_data)
    input_data = list(input_json['image_data'])
    input_data = ''.join(input_data[2:-1])
    # Convert image from base64 string to int
    input_data = base64.b64decode(bytes(input_data, 'utf-8'))
    # Transforms for ML model input
    input_data = transform_image(input_data)

    filename = input_json['filename']

    classes = ['normal', 'suspicious']

    # get prediction
    with torch.no_grad():

        output = model(input_data)
        softmax = nn.Softmax(dim=1)
        pred_probs = softmax(output).numpy()[0]
        index = torch.argmax(output, 1)

    # This will be the message to IoT Hub
    result = {"label": classes[index], 
              "probability": str(pred_probs[index]),
              "filename": filename}

    return result