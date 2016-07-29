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

rows,cols = img.shape[:2]
  
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
   
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Translated')
plt.xticks([]), plt.yticks([])

# Save the output in a figure
plt.savefig(sys.argv[2]);
#plt.show()
