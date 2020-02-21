from PIL import Image
import sys


def resizeImage(img):

    im = Image.open(img)
    h, w = im.size

    if h < w:
        size = h
        box = ((w - h) / 2, 0, w - (w - h) / 2, h)
    elif h > w:
        size = w
        box = (0, (h - w) / 2, w, h - (h - w) / 2)
    else:
        print("The image is already a square")

    newimg = im.crop(box)
    newimg.save('newimg.jpg')



if __name__ == '__main__':

    img = sys.argv[1]
    resizeImage(img)
    print('The Picture has been squared!!')

    #print(img)


