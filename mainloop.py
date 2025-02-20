# rough outline for the main loop 

# import libraries and functions
import random # temporary
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import morphology
from util.img_util_example_solution import ImageDataLoader as IDL
from util.inpaint_util import removeHair as rH


# set up data loader and an iterator for it
data_loader = IDL("data/Data", shuffle=False)
data_iterator = iter(data_loader)

# loop through the images
for _ in range(len(data_loader)):

    img_rgb, img_gray, img_name = next(data_iterator)

    # filter out the hair
    _, _, img_noHair = rH(img_rgb, img_gray)

    # scale the values appropriately (they are defaulted to be from 0 to 1)
    img_scaled = rgb2gray(img_noHair) * 256
    
    # create and refine the mask
    im_mask = img_scaled <= 120
    struct_el = morphology.disk(2)
    mask_dilated = morphology.binary_erosion(morphology.binary_dilation(morphology.binary_dilation(im_mask, struct_el), struct_el), struct_el)

    # apply the updated mask onto the image
    img_noHair[mask_dilated==0] = 0

    # calculate other needed values

    # compute final score
    score = random.randint(0, 100) / 100 # placeholder

    # print out result 
    print(f'{img_name} score: {"{:.2f}".format(score)}.', end= '')
    
    # all placeholder thresholds
    if score < 0.11: 
        print(' Not cancerous.')
    elif score < 0.46:
        print(' Moderate risk of cancer.')
    elif score < 0.76:
        print(' Considerable risk of cancer.')
    elif score < 0.79:
        print(' Most likely cancer.')
    else:
        print(' Cancerous.')