# Mariana Ponce Gonzàlez
# Misiòn 4 Imagenes

from PIL import Image

#Leer imagen de 800x800
def cargarImagen(archivo):
    img = Image.open(archivo)
    return img

#Invertir o voltear
def cargarimg(i):
    if i == "Invertir":
        im = ImageOps.invert(imagen)
    else:
        im = ImageOps.flip(imagen)
    
def main():
    image = cargarImagen("ej.jpg")
    image.show()
    a = input("Dame la instrucciòn ")
    imag = cargarimg("a")
    imag.show()
    

    
main()



