#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2017, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# hsv_binary.py
#
# Author : sosorry
# Date   : 08/30/2016
# Usage  : python hsv_binary.py

import cv2
import numpy as np

image = cv2.imread("CROP.jpg")

# Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define range of purple color in HSV
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])


# Threshold the HSV image to get only purple colors
binary = cv2.inRange(hsv, lower, upper)
cv2.imshow("Binary", binary)
print "HSV Binary image..."
cv2.waitKey(0)

cv2.destroyAllWindows()

