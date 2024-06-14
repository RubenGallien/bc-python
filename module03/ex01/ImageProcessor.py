import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageProcessor:
    def load(self, path):
        if isinstance(path, str):
            im_frame = Image.open(path)
            if im_frame:
                print(f"Loading image of dimensions {im_frame.width} x {im_frame.height}")
                return np.array(im_frame, float)
            else:
                print("Image can't be read")
        return None


    def display(self, array):
        img = None
        plt.axis("off")
        img = plt.imshow(array)
        plt.show()