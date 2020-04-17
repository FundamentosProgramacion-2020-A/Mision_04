# Mariana Ponce Gonzàlez
# Misiòn 4 Imagenes

from PIL import Image, ImageOps

#Leer imagen de 800x800
def cargarImagen(archivo):
    img = Image.open(archivo)
    return img

#Invertir o voltear
def cargarimg(i,imagen):
    if i == "Invertir":
        im = ImageOps.invert(imagen)
    else:
        im = ImageOps.flip(imagen)
        return im
    
def main():
    image = cargarImagen("ej.jpg")
    image.show()
    a = input("Dame la instrucciòn ")
    imag = cargarimg(a,"ej.jpg")
    imag.show()
    
main()



