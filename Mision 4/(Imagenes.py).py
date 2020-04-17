# Autor: Miguel Castillo Ordaz
# Muostrar una imagen, inviertela y voltearla.

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
    imagen = cargarImagen("The Tree of Life 2.jpg")
    imagen.show() #Muestra la imagen en la pantalla
    
    img = input("Esta imagen quieres que sea, ¿invertirla o voltearla?: ")
    
    if img == "invertirla":
        invertir =invertirImagen(imagen)
        invertir.show()
    else:
        if img == "voltearla":
            voltear = voltearImagen(imagen)
            voltear.show()
            
main ()