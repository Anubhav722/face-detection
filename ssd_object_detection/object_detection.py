# Importing the libraries

import torch
from torch.autograd import Variable

import cv2 # for drawing rectangles

from data import BaseTransform, VOC_CLASSES as labelmap

from ssd import build_ssh
import imageio

# Define the detect function

def detect(frame, net, transform):
    """
    net is ssd neural network.
    transform is used here for transforming the images to the right format.
    """
    
    height, width = frame.shape[:2] # three arguments. height , width and the channels are returned by the function shape
    # black and white image has channel 1. and the colored image has channel as 3 (BGR).
    
    # Perform a series of transformations to frame to get a torch variable.
    # Or series of transformations to make before feeding into the neural network
    

    # First transformation.
    frame_t = transform(frame)[:0]
    # returns frame in the right format in the form of numpy array
    
    # Second transformation
    # Converting the numpy array into the torch tensor.
    # Torch tensor is a much more advanced matrix than the numpy array.
    x = torch.from_numpy(frame_t).permute(2, 0, 1)
    # It is converting the sequence red, blue, green into the sequence green, red, blue.

    
    # Third transformation
    # Add this fake dimension corresponding to the batch.
    # Neural network cannot accept the single input vector or single input image.
    # Neural network only accepts batches of inputs.
    # x.unsqueeze(0)

    
    # Fourth transformation
    # Converting the torch sensor function to torch variable.
    # Torch variable is a highly advanced variable which contains both a tensor and gradient.
    x = Variable(x.unsqueeze(0))
