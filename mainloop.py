# rough outline for the main loop 

# import libraries and functions
import random # temporary
import numpy as np
import matplotlib.pyplot as plt
from util.img_util_example_solution import ImageDataLoader as IDL
from util.mask_applier import mask_applier


# set up data loader and an iterator for it
data_loader = IDL("data/Data", shuffle=False)
data_iterator = iter(data_loader)

# loop through the images
for _ in range(len(data_loader)):

    img_rgb, img_gray, img_name = next(data_iterator)

    # use apposit function to filter out hair, create a mask and then to apply it
    img_noH_masked = mask_applier(img_rgb, img_gray)

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