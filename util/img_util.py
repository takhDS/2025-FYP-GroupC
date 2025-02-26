import os
import random
import pandas as pd
import cv2


def readImageFile(file_path):
    # read image as an 8-bit array
    img_bgr = cv2.imread(file_path)

    # convert to RGB
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

    # convert the original image to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

    return img_rgb, img_gray


def saveImageFile(img_rgb, file_path):
    try:
        # convert BGR
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # save the image
        success = cv2.imwrite(file_path, img_bgr)
        if not success:
            print(f"Failed to save the image to {file_path}")
        return success

    except Exception as e:
        print(f"Error saving the image: {e}")
        return False


class ImageDataLoader:
    def __init__(self, directory, shuffle=False, transform=None,groupid="C"):
        self.directory = directory
        self.shuffle = shuffle
        self.transform = transform
        self.groupid = groupid
        
        df = pd.read_csv("data-student.csv")
        # get a sorted list of all image files assigned to Group C in the directory
        self.file_list = sorted(
            [os.path.join(directory, f) for f in os.listdir(directory) if
            (f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))) and not df[df["File_ID"] == f].empty  
            and self.groupid in df[df["File_ID"] == f]["Group_ID"].values]
        )

        if not self.file_list:
            raise ValueError("No image files found in the directory.")

        # shuffle file list if required
        if self.shuffle:
            random.shuffle(self.file_list)

        # get the total number of files
        self.num_sample = len(self.file_list)
        
    def __len__(self):
        return self.num_sample

    def __iter__(self):
        for file_path in self.file_list:
            img_rgb, img_gray = readImageFile(file_path)

            if self.transform:
                img_rgb = self.transform(img_rgb)
                img_gray = self.transform(img_gray)
            #also yield the name so that we can save the file easier
            name = file_path.split("\\")[-1]

            yield img_rgb, img_gray, name