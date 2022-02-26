
from sys import argv,stdin
from PIL import Image, ImageDraw, ImageFont

img =Image.open("C:/Users/nadir/Desktop/sprint-crypto-26/amphi1-Cake/cake.png")
w,h=img.size
maskR=Image.new('L', (w,h), color=255)
maskG=Image.new('L', (w,h), color=255)
maskB=Image.new('L', (w,h), color=255)
maskRGB=Image.new('L', (w,h), color=255)
def dechiffrementStegano(x):
    return 255*(x%2)

for i in range(h):
    for j in range(w):
        (r,g,b)= img.getpixel((j,i))
        maskR.putpixel((j,i), dechiffrementStegano(r))
        maskG.putpixel((j,i), dechiffrementStegano(g))
        maskB.putpixel((j,i), dechiffrementStegano(b))
        maskRGB.putpixel((j,i), min(dechiffrementStegano(r), dechiffrementStegano(g), dechiffrementStegano(b)))

    maskR.save('C:/Users/nadir/Desktop/sprint-crypto-26/amphi1-Cake/Y.png')
    maskG.save('C:/Users/nadir/Desktop/sprint-crypto-26/amphi1-Cake/X.png')
    maskB.save('C:/Users/nadir/Desktop/sprint-crypto-26/amphi1-Cake/Z.png')
    maskRGB.save('C:/Users/nadir/Desktop/sprint-crypto-26/amphi1-Cake/YXZ.png')
