import matplotlib.pyplot as plt
#import numpy as np
import cv2
import matplotlib.image as mpimg

#Read image
#image size (490, 655, 3) in uint8 datatype
img = mpimg.imread('car.jpeg')


#To print image dimensions
print 'Image dimensions  = ', img.shape
#Convert image from RGB to GRAY
#image size  will be (490, 655) in uint8 datatype
grayimg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

plt.imshow(grayimg, cmap='gray')

# Print specific grayscale pixel values
# What is the pixel value at x = 400 and y = 300 (on the body of the car)?

x = 400
y = 300
pixel_value = grayimg[x,y]
print 'pixel value: ',pixel_value
