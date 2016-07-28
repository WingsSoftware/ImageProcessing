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
 
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
 
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

# Save the output in a figure
plt.savefig(sys.argv[2]);
#plt.show()
