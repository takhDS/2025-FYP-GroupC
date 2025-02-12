import cv2
import numpy as np

from PIL import Image
from IPython.display import display
from matplotlib import pyplot as plt

class imgmanip:
    def __init__(self):
        self.image = None
    

    # function loads an image from path
    def imgload(self, path):
        try:
            self.image = Image.open(path)
            print("Image loaded sucessfully.")
        except Exception as e:
            print(f"Error loading image: {e}.")
    

    # function loads an image from OpenCV
    def imgload_opencv(self, path):
        try:
            self.image = cv2.imread(path)
            print("Image loaded sucessfully.")
            print("The size of the input image is: ", self.image.shape())
        except Exception as e:
            print(f"Error loading image: {e}.")
    

    # function prints the path image
    def imgdisplay(self):
        if self.image:
            display(self.image)
        else:
            print("No image to display.")
    

    # function creates an array from the path image
    def imgtoarray(self):
        if self.image:
            imgnp = np.array(self.image, dtype=np.uint8)
            print("Image converted to array.")
            print("The size of the input image is: ", imgnp.shape())
            return imgnp
        else:
            print("No image loaded to convert.")

    
    # function converts OpenCV from BGR to RGB
    def BGRtoRGB(self):
        if self.image:
            imageRGB = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            print("Image channel converted to RGB.")
            return imageRGB
        else:
            print("No whose channel image to convert.")


    # function converts from BGR image to grayscale
    def grayscale(self):
        if self.image:
            imagegray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            print("Image converted to grayscale.")
            return imagegray
        else:
            print("No imgage to convert to grayscale.")
    

    # def plot RGB image of cv2

    # def plot greyscale image