import glob
import os
import sys

import cv2 as cv
import numpy as np


def removelines(img):
    img1 = cv.imread(img)  # reading the image from path that received from the function arguments
    hvs_img = cv.cvtColor(img1, cv.COLOR_BGR2HSV)  # changing the color of the image from BGR model to HSV model
    lower_yellow = np.array([21, 39, 114])  # getting the lower level of yellow color in HSV model
    upper_yellow = np.array([40, 255, 255])  # getting the highest level of yellow color in HSV model
    mask = cv.inRange(hvs_img, lower_yellow, upper_yellow)  # creating the mask of the yellow lines from the image
    mask_inv = cv.bitwise_not(mask)  # created inverted mask from the mask that created
    img1_bg = cv.bitwise_and(img1, img1, mask=mask_inv)  # using the mask that created and bitwise  "and operator " to
    # create the background
    img2_fg = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)  # because the mask is GRAYSCALE that mean its 1 channel
    # and the cv.add need to be same number of channels , using cvtColor switch from GRAYSCALE to BGR and the mask
    # became 3 channels
    dst = cv.add(img1_bg, img2_fg)  # merging the two images ( mask and HSV image ) to get the final result
    return dst


def loopRun(inputs, output):
    path = os.path.basename(inputs)  # getting the basename from the path that received
    # e.g. C:\Users\amara\Desktop\new => new

    output = os.path.normpath(output)  # changing the format of path that received
    # from String format to path
    # e.g. C:\Users\amara\Desktop\new => C:\\Users\\amara\\Desktop\\new
    for img in glob.glob(path + "/*.jpg"):  # loop to get every image in the dir
        filename = os.path.basename(img)  # getting the file name (image name )
        fixed_image = removelines(img)  # receiving the image after removing the yellow lines
        cv.imwrite(output + '\\' + filename, fixed_image)  # writing (saving) the image to the path


if __name__ == "__main__":
    inputPath = sys.argv[1] # getting the input path from the command line
    outputPath = sys.argv[2] # getting the output path from the command line
    if os.path.isdir(inputPath): # checking if the input string is an exist path
        if os.path.isdir(outputPath):  # checking if the output string is an exist path
            loopRun(inputPath, outputPath)
        else:
            print("output dir is not valid ")
    else:
        print("input dir is not valid ")
