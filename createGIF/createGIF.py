import imageio
import os

#create gif function
def createGif(imageFolder, gifName, duration):
    #array to store images
    images = []
    #loop to go through each image in folder named frames
    for filename in sorted(os.listdir(imageFolder)):
        #use files if ending with .png or .jpg
        if filename.endswith(".png") or filename.endswith(".jpg"):
            #append each image into images array
            images.append(imageio.imread(os.path.join(imageFolder, filename)))
    
    imageio.mimsave(gifName, images, duration=duration)

imageFolder = "frames"
gifName = "result.gif"
duration = 0.2 #change here
#add variables to function
createGif(imageFolder, gifName, duration)