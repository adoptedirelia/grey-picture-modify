import torch
import cv2
import numpy as np

pic = cv2.imread('./irelia.jpg')
pic = pic.sum(axis=2)//3
