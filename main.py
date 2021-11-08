import glob

import cv2
import matplotlib.pyplot as plt
import numpy as np

import os

import cv2
import matplotlib.pyplot as plt
import numpy as np

n = cv2.imread('text_regions/BRN3C2AF4AEB56C_0000000015.jpg')
hvs_img = cv2.cvtColor(n,cv2.COLOR_BGR2HSV)
lower_yellow = np.array([21,39,64])
upper_yellow = np.array([40,255,255])


mask = cv2.inRange(hvs_img,lower_yellow,upper_yellow)
new_mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
new_image = cv2.bitwise_and(new_mask,hvs_img)
plt.imshow(new_image,cmap='gray')
plt.show()



# for img in glob.glob("text_regions/*.jpg"):
#     n= cv2.imread(img,1)
#
#     filename = os.path.basename(img)
#     path = 'D:\\'
#     cv2.imwrite(path + filename , n)
#
