'''
This script get average color of a grey-scale image
'''
import cv2
import numpy

myimg = cv2.imread('faces/01F_NE_C - Copy-02.png')
avg_color_per_row = numpy.average(myimg, axis=0)
avg_color = numpy.average(avg_color_per_row, axis=0)
print(avg_color)