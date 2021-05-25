import sys
import PIL
from PIL import Image
import os

list_im = []

for filename in os.listdir(os.getcwd( )):
    if filename[filename.rfind(".") + 1:] in ['jpg', 'jpeg', 'png']:
        list_im.append(filename)
        print(list_im)

basewidth  = 100
baseheight  = 100


for image in list_im:
    img = Image.open(image)
    if img.size[0] > img.size[1]:
        ratio = (basewidth / float(img.size[0]))
        height = int((float(img.size[1]) * float(ratio)))
        img = img.resize((basewidth, height), PIL.Image.ANTIALIAS)
        new_img = img.save(image)
        background = Image.open('Kartinka.jpg')
        bg_w, bg_h = background.size
        offset = ((bg_w - img.size[0]) // 2, (bg_h - img.size[1]) // 2)
        background.paste(img, offset)
        background.save(image)

    else:
        hpercent = (baseheight / float(img.size[1]))
        width = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((width, baseheight), PIL.Image.ANTIALIAS)
        new_img = img.save(image)
        background = Image.open('Kartinka.jpg')
        bg_w, bg_h = background.size
        offset = ((bg_w - img.size[0]) // 2, (bg_h - img.size[1]) // 2)
        background.paste(img, offset)
        background.save(image)





