from util.inpaint_util import removeHair as rH
from skimage.color import rgb2gray
from skimage import morphology 

def mask_applier(img_rgb, img_gray):
    """Removes hair from the given image, creates and apply a mask to
    individuate the lesion.
    The grayscale image should have pixel values between 0 and 1, as they
    will be scaled up appropriately by the function.
    
    :param img_rgb: the rgb original image
    
    :param img_gray: the grayscale original image
    
    :return: hairless, masked rgb image"""

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

    return img_noHair