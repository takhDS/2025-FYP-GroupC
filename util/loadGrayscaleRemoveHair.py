#loads all images from the data folder and uses the template code to remove the hair -> saves them straight to the utils folder

#necessary imports
import img_util_example_solution as loadUtils
import inpaint_util as ipUtils

import matplotlib.pyplot as plt
from pathlib import Path

#get the root directory for the repository
root_dir = Path(__file__).resolve().parent.parent
#initialize the imageDataLoader with the data folder
dataLoader = loadUtils.ImageDataLoader(str(root_dir) + "\\data\\Data")

for imgColor, imgGray, name in dataLoader:
    blackhat, thresh, img_out = ipUtils.removeHair(imgColor, imgGray)
    loadUtils.saveImageFile(img_out, "noHair_" + name)