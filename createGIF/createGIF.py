import imageio
import os

# create gif function
def createGif(imageFolder, gifName, duration):
    # array to store images
    images = []
    # loop to go through each image
    for filename in sorted(os.listdir(imageFolder)):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            images.append(imageio.imread(os.path.join(imageFolder, filename)))
    
    imageio.mimsave(gifName, images, duration=duration)

imageFolder = "frames"
gifName = "result.gif"
duration = 0.2

createGif(imageFolder, gifName, duration)