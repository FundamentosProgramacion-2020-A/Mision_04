# Autor: Patricio León
# Muestra una imagen y de misma forma inviertela y volteala


# De la libreria PIL, importamos Image
from PIL import Image, ImageOps     


def cargarImagen(archivo):
    img = Image.open(archivo)
    return img


def invertirImagen(imagen):
    invertir = ImageOps.invert(imagen)
    return invertir


def voltearImagen(imagen):
    voltear = ImageOps.flip(imagen)
    return voltear


def main():
    imagen = cargarImagen("Lobo.jpg")
    imagen.show()     #Muestra la imagen en la pantalla

    img = input("Esta imagen quieres que sea, ¿invertirla o voltearla?: ")
    
    if img == "invertirla":
        invertir = invertirImagen(imagen)
        invertir.show()
    else:
        if img == "voltearla":
            voltear = voltearImagen(imagen)
            voltear.show()
    
    
# Llama a la función principal para resolver el problema 
main ()    