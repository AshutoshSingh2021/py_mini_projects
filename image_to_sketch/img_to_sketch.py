import numpy as np
import cv2
from scipy.ndimage import gaussian_filter
import imageio.v2 as imageio

img = "./image_to_sketch/fullsize.jpg"

def convert_to_gray(coloured_img):
    # taking the array representation of the coloured image [red, green, blue, other dimensions(excluded)] and myltiplying it with some value and returning the changed color weights
    return np.dot(coloured_img[..., :3], [0.1989, 0.5870, 0.1240])

def dodge(blur, gray):
    final_sketch = blur*255/(255-gray)
    # if any value in the image is greater than 255 which is almost impossible but still if it is there we will convert it to 255
    final_sketch[final_sketch>255] = 255
    final_sketch[gray == 255] = 255
    return final_sketch.astype('uint8')

source_image = imageio.imread(img) # reading the input image
gray_scale =  convert_to_gray(source_image)

# subtracting the gray_scale rgb values from brightest color (255) to make it closer to black 
intensity = 255-gray_scale 

# apply blur filter "https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html#scipy.ndimage.gaussian_filter" (Play with the parameters of the filter and see varrying results)
blur_img = gaussian_filter(intensity, sigma=30)

# blend the blur image and gray image to create a beautiful sketch 
result_img = dodge(blur_img, gray_scale)

# write the 8-bit int format into a png file
cv2.imwrite('result-sketch.png', result_img)