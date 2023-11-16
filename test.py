from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt


np.set_printoptions(threshold=sys.maxsize)

path1 = "/Users/hb/Downloads/drive-download-20221219T055151Z-001/3310.png"
img1 = Image.open(path1)
a = np.array(img1)

path2 ="/Users/hb/Downloads/drive-download-20221219T035237Z-001/3310.png"
img2 = Image.open(path2)
b = np.array(img2)


plt.imshow(a)
#alpha는 투명도
plt.imshow(b,alpha = 0.5)
plt.show()