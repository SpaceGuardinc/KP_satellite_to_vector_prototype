from distutils.log import error
import cv2
from sklearn.feature_extraction import image

x = [[]]
y = [[]]
z = [[]]

image = cv2.imread("/images/1.jpd")
if(image == None):
    print(error)
image[x,y,z]
print(image[::])