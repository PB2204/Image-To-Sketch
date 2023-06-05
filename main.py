#Install imageio package
# %pip install imageio

# matplotlib inline
import imageio
import requests
import matplotlib.pyplot as plt
import IPython.display as dp
import fileinput

#Display the image from the web using an URI.
# img = "https://blogger.googleusercontent.com/img/a/AVvXsEjw-bw_NBVbhkhDSL4IPmLJnk27eeU3-mk66p4IS9pB7eKirs3VLxUJcBUiRchtVLjaEvy9T8R1P2Z_QXqLvzGockmaZNcjCozBCa8IlRvF-Fcmxmv3w9wiKxMv8ciAgC6TUopPahgGg7RW8Jem3w35PZhthT-txN9JAA0l5FCCg_pzd344_wZPQa8VTg=s418"
# dp.Image(requests.get(img).content)

# Prompt the user to enter the file path of the image
file_path = input("Enter the file path of the image: ")

# Read the image file
with open(file_path, 'rb') as f:
    img = f.read()

# Display the image
dp.Image(img)


#Read the image using imgaeio package's imread method and URI from web using 
source_img = imageio.imread(img)


# Make the image Black and White using the formula Y= 0.299*R + 0.587*G + 0.114*B i.e. applying greyscale
import numpy as np

def grayscaleimg(rgb): 
  return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

gryscl_img = grayscaleimg(source_img)


#Invert the image by subtracting it from 255
inv_img = (255 - gryscl_img)
plt.imshow(inv_img)

#Blur the image using gaussian filter
import scipy.ndimage
blurred_img = scipy.ndimage.filters.gaussian_filter(inv_img, sigma=5)
plt.imshow(blurred_img)


#Create function to perform dogding(belnding together greyscale and blurred image)
def dodging(blur_img, gryscl_img):
    resultant_dodge=blur_img*255/(255-gryscl_img) 
    resultant_dodge[resultant_dodge>255]=255
    resultant_dodge[gryscl_img==255]=255
    return resultant_dodge.astype('uint8')


#Generate the target image by applying the dodge
target_img= dodging(blurred_img, gryscl_img)


#Display the target image
# %matplotlib inline
import matplotlib.pyplot as plt
plt.imshow(target_img, cmap="gray")


#Save the image
plt.imsave('target_image.png', target_img, cmap='gray', vmin=0, vmax=255)