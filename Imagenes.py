# Autor: Fernando Pérez González
# Cargar imagen y preguntarle al usuario si quiere
# invertirla o voltearla verticalmente

from PIL import Image, ImageOps

def cargarImagen(archivo):     #carga la imagen
    img = Image.open(archivo)
    return img


def invertirImagen(imagen):    #invierte los colores de la imagen
    img = ImageOps.invert(imagen)
    return img
    
    
def voltearImagen(imagen):     #voltea la imagen
    img = ImageOps.flip(imagen)
    return img
    
    
def main():
    imagen = cargarImagen("Salmita.jpg")
    imagen.show()
    
    queHacer = input("¿Quieres invertir los colores o voltear imagen, escribe únicamente invertir o voltear?: ")
    
    if queHacer == "invertir":
        invertir = invertirImagen(imagen)
        invertir.show()
    elif queHacer == "voltear":
        voltear = voltearImagen(imagen)
        voltear.show()
    else:
        print("Error, inténtalo de nuevo")
     
main()