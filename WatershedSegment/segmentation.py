# Add OpenCV to the path
import sys
sys.path.append('/usr/local/lib/python2.5/site-packages/')

# Import OpenCV
import cv2

# Import NumPy
import numpy as np

# Read the argument passed to python
img = cv2.imread(sys.argv[1])
#img = cv2.imread('water_coins.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# noise removal
kernel = np.ones((1,1),np.uint8)
morph = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations=2)

# create binary image
(h, w) = img.shape[:2]
binary = np.zeros((h, w), np.uint8)
binary += -1
binary[morph==255] = 0
binary[morph==0] = 255

wskernel = np.zeros((2,2),np.uint8)
wskernel += -1
# foreground area
fg = cv2.erode(binary,wskernel,iterations=3)

# background area
bg = cv2.dilate(binary,wskernel,iterations=3)
ret, bg = cv2.threshold(bg, 1, 128, cv2.THRESH_BINARY_INV)

markerimg = fg + bg
markers = np.zeros((h, w), np.int32)
for (x,y), value in np.ndenumerate(markerimg):
	markers[x][y] = value

cv2.watershed(img, markers)
cv2.imwrite(sys.argv[2], markers)

