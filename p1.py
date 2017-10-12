import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2


image = mpimg.imread('test_images/solidWhiteRight.jpg')

print('This image is:', type(image), 'with dimensions:', image.shape)
plt.imshow(image)