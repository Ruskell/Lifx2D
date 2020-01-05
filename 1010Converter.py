#Author: Ruskell

from skimage import io, img_as_float
import numpy as np
import image_slicer as ims
from PIL import Image
import os
import glob

TILE_HEIGHT = 3
TILE_WIDTH = 2
TILE_DIM = 8

TOTAL_WIDTH = TILE_DIM * TILE_WIDTH
TOTAL_HEIGHT = TILE_DIM * TILE_HEIGHT

IMG_LOC = "F:\Projects\Lifx2D\\1010Converter\\firstRound1.jpg"

def Crop(im, width, height):
        imgwidth, imgheight = im.size
        for i in range (imgheight//height):
                for j in range (imgwidth//width):
                        box = (j*width, i*height, (j+1)*width, (i+1)*height)
                        yield im.crop(box)


def AvgColour(image):
        r, g, b = 0, 0, 0
        count = 0
        imgWidth, imgHeight = image.size
        
        for wid in range (0, imgWidth):
                for hei in range (0, imgHeight):
                        pixr, pixg, pixb = image.load()[wid, hei]
                        r += pixr
                        g += pixg
                        b += pixb
                        count += 1
        return ((r/count), (g/count), (b/count))


image = Image.open(IMG_LOC)
imgwidth, imgheight = image.size
print ('Image size is: %d x %d ' % (imgwidth, imgheight))

width = round(imgwidth / TOTAL_WIDTH)
height = round(imgheight / TOTAL_HEIGHT)
print ('Individual img size is: %d x %d ' % (width, height))
print ('Tile size is: %d x %d ' % (TOTAL_WIDTH, TOTAL_HEIGHT))


for x in range(0, TOTAL_WIDTH):
        for y in range(0, TOTAL_HEIGHT):
                crop = Crop(image, width*x, height*y)
                #print (x*y, crop)

                img = Image.new('RGB', (width, height), 255)
                #print (img)

                print(AvgColour(img))


#for k, piece in enumerate(Crop(image, height, width), 0):
#       print (k, piece)
#       
#       img = Image.new('RGB', (width, height), 255)
#       print (img)


#def ConvertImg(img):
	#blah
	
	
