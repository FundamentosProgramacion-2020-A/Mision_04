#Autor: Elena R.Tovar A01376318
#Permitir al usuario hacer edición de imagen
from PIL import Image, ImageOps

def loadImg(arch):
    img=Image.open(arch)
    return img

def invertImage(arch):
    img=ImageOps.invert(arch)
    return img

def flipImage(arch):
    img=ImageOps.flip(arch)
    return img

def main():
    img= loadImg("cedetec.jpeg")
    img.show()
    instruction= int(input("""Elija lo que desea hacer con la imagen
    Para obtener el negativo, presione 1.
    Para voltear verticalmente, presione 2"""))
    if instruction == 1:
        dimg=invertImage(img)
        dimg.show()
    elif instruction==2:
        cimg=flipImage(img)
        cimg.show()
    else:
        return ERROR
main()