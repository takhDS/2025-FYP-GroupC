# Projects in Data Science (2025)
## Summary

The goal of this summary is to present the overall essence of our code and its interaction with the provided data sample, outlining important features of its usage. First, we will briefly present the structures of our code and their purposes.

1. **Data Loader** - Object of our IDL class which takes a directory as argument and grants us access to the images in the specific folder, for further analysis.
2. **Data Iterator** - Contains the result of the iteration function applied on our loaded data.
3. **The For Loop** should run over all images of our data set, and for each, uses the function "next()" on the data iterator to output the colroed version of the image, the grayscale one, and the name of the file we're currently viewing. This last variable was our addittion to the sample code provided, as we thought knowing what image we're dealing with will be important in case we would want to export said image.
4. **Hair Removal Function** - This function was provided for us by our project coordinators, and as we had nothing to tweak at it, we imported and used it. This function outputs the black hat version, the threshold of the image's grayscale and the actual image with the hair removed. The function requires both the colored and grayscale versions as parameters, which we cnveniently obtained previously from the iterator.


Next, we will dive into the obtained information from our data base and show some examples of the functionalities as well as discuss strong and weak spots within our code.


## Correct Example
Visually and theoretically, this is an example of a usual and correct result obtained from our program:
Here is the image of mole 50, with successfully removed hair.
![img_50](summary_images\img_50.png "Mark with correctly removed hair")

Our code also has the ability to plot a histogram of the hues of the image, which we do after the hair removal, so that the strands don't interfere with our analysis. Leaving hair in could potentially spike the occurence of dark hues in our plot. It is clear, that the image's values are quite balanced, which might be an important clue in the medical field.
![img_50_hist](summary_images\img_50_hist.png "Correct example of a histogram")

The next step in our code, is creating a mask, that will cut away the skin and only leave the potential cancerous mark in the frame. This mask, will be plotted over the image with removed hair. A correct mask should look something like this, with clear, defined lines around the edges, and attention to detail; it's important that the mask doesn't remove crucial parts of our mole.
![img_50_mask](summary_images\img_50_mask.png "Correct example of a mask")

Lastly, this is how the final result of our code looks; an isolated, hairless mole, ready to be passed to the doctors in charge of diagnosis.
![img_50_masked](summary_images\img_50_masked.png "Correct example of a masked mole")


## Issue #1 - Brightness Distinction
One of the issues we primarily noticed in our program, is the fact that it struggles with identifying moles which are of the same brightness and color as the healthy skin around it. Since we used the suggested threshold of 120, not all of the lesion images are masked correctly by the machine. This appears to be caused by the natural difference in hue and shade of the skin, as not all provided lesions have a contrasting color difference between healthy and sick skin.

In the example of the 70th mole, it can be observed that the color of skin is pretty uniform. 
This is the image we are working with (hair has been removed in advance):
![img_70](summary_images\img_70.png "Image Issue #1")

Now shifting our attention to the masked version, we can see that the lesion itself has been successfully circled, however the mask also selected some darker patches of skin off the bottom left corner, which seem to be nothing more than a variance in color. If this were to be considered part of the lesion, it would mean false information.
![img_70_mask](summary_images\img_70_masked.png "Image Issue #1")

This example of machine error, flashes a light on the weak spots of our code. When the potential melanoma is of a similar color to the healthy skin found around the lesion, the program might mistake this for illness.

Further insight into this topic, may be offered by the histogram of the grayscale, which is seemingly quite concentrated on the mid-range, left skewed, with drastically uneven tails. The lack of variety in shades seems to be the reason our masking function is having trouble with this image.
![img_70_hist](summary_images\img_70_hist.png "Image Issue #1")
Perhaps for future reference the histogram could be used to predict the accuracy of which the program can select the mark on the skin.

## Interesting Contrast
To contrast the previous observation, we will take another example from our data sample. Even to the human eye the shade difference between the healthy skin and the possible cancerous patch is much more visible.
![img_5](summary_images\img_5.png "Contrasting Example")

If we look at the histogram for the image version without hair, we notice how the dark hues spike very far on the right, while the rest of the skin maintains a somewhat low and constant range. This type of spread-out histogram could be an indicator of an accurate depiction of masking.
![img_5_hist](summary_images\img_5_hist.png "Contrasting Example Histogram")

Now let's focus on the masked version:
![img_5_masked](summary_images\img_5_masked.png "Contrasting Example Masked")
It’s particularly interesting how the mask takes a chunk out of the centre of the lesion. At first glance it might look wrong, but analysing the original image once again, it becomes clear, that that patch might actually be healthy skin! The fact that the discoloured patch isn’t uniformly spread on the surface of the skin, might be an important indicator to specialists on how the patch progresses in time.

This reveals a strong suit of our program; it is the sensitivity to changes within the lesion. If monitored over a longer period of time, multiple masks of the same lesion can uncover insightful progression stamps and perhaps even help predict the progression of certain diseases. We’d like to compare this to a weather map chart showcasing the movement of clouds.

## Issue #2 - Color Change

We have unfortunately come across a second fault in our code, and that is the discoloration of the mole once it's run through the hair removal function.

This issue occurs when the hair is very thick or dense covering the mole and the program must guess what the underlying hues are. However, in it's process of blending out the hair strands, it also strips the mole of its significant color, possibly telling for the diagnosis. Used in real life, this could be a serious issue and lead to innaccurate analysis.
Let's compare the two:
![img_36](summary_images\img_36.png "Color Change Example")
![img_36_nohair](summary_images\img_36_nohair.png "Color Change Example")
As can be seen, the edited image is much lighter, the patches around the lesion itself are gone, and so are the scabs present atop of the scar.

Moreover, the effect of the faulty hair removal snowballs onto the result of the mask, which is a very butchered version of the original image, the shape looks nothing like the original. In the real world, such errors are dangerous.
![img_36_masked](summary_images\img_36_masked.png "Color Change Example")

## Conclusion
Lastly, it's obvious that with more time on our hands the errors found could be fixed, the code resultingly perfected into a usable model for the medical field and not only.

This type of image manipulation code can have numerous uses in different fields and, as such, we feel that our hands on experience with such exercises might turn out to be a meaningful experience.