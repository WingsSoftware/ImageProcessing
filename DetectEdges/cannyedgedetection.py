# Add OpenCV to the path
import sys
sys.path.append('/usr/local/lib/python2.5/site-packages/')

# Import OpenCV
import cv2

# Import NumPy
import numpy as np

# Import Matplotlib
import matplotlib
# Force matplotlib to not use any Xwindows backend
matplotlib.use('Agg')

# Import pyplot
from matplotlib import pyplot as plt

# Read the argument passed to python
img = cv2.imread(sys.argv[1])
edges = cv2.Canny(img,100,200)
  
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
  
plt.show()

# Save the output in a figure
plt.savefig(sys.argv[2]);
#plt.show()
