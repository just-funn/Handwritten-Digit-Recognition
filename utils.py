import cv2
import numpy as np


def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def resize_image(image, width, height):
    return cv2.resize(image, (width, height))


def normalize_image(image):
    return image / 255.0


def invert_colors(image):
    return cv2.bitwise_not(image)
