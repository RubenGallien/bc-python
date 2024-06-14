from ImageProcessor import ImageProcessor
from PIL import Image

path = "42ai_logo.png"
obj = ImageProcessor()
arr = obj.load(path)
obj.display(arr)