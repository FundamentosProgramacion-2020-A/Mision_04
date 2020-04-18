#José Manuel Rivera Sosapavón
#Imagenes
#Escribe un programa que carga una imagen (tamaño cercano a 800x800).
#Posteriormente le pregunta al usuario la operación que quiere realizar:
#1. Invertir. Calcula el negativo de la imagen. Usa la función invert de la clase ImageOps de PIL.
#2. Voltear verticalmente. Usa la función flip de la clase ImageOps de PIL. No olvides mostrar la imagen original
#y la modificada en la pantalla.

from PIL import Image, ImageOps

def cargarImagen(archivo):
    imagen = Image.open(archivo)
    return imagen


def invertirImagen(imagen):
    imginvert = ImageOps.invert(imagen)
    return imginvert


def voltearVertical (imagen):
    flip = ImageOps.flip(imagen)
    return flip

def main ():
    imagen = cargarImagen("amaricooper.jpg")
    imagen.show()
    
    
    foto = input("¿Desea voltear o invertir la imagen? ")
    if foto == "invertir":
        invert = invertirImagen(imagen)
        invert.show()
    else:
        if foto == "voltear":
            volteada = voltearVertical(imagen)
            volteada.show()
    
    
    
    
    
main()
    
