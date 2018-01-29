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
    
