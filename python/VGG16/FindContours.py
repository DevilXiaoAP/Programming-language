import PIL.ImageOps
from PIL import Image
import cv2 as cv
import numpy as np
from scipy import io
img = Image.open('F:/Study/代码/python/VGG16/2.1.jpg')
img = img.convert('1')
#img.show()


img = img.convert('L')
img = PIL.ImageOps.invert(img)
img = img.convert('1')
#img.show()
img.save('3.1.jpg')
np.save('img1.npy',img)
mat = np.load('img1.npy')
io.savemat('gene_features1.mat', {'gene_features': mat})