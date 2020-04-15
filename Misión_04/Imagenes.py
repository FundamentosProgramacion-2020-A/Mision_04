# Autor: Paloma Argelia Cueto González
# Programa que carga una imagen y pregunta al usuario que quiere hacer

# De la librería PIL, hay que importar imagen
from PIL import Image, ImageOps

# Cargar imagen
def cargarImagen (archivo):
    img = Image.open(archivo)
    return img

# Modificaciones a la imagen
def invertirImagen (imagen):
    invertir = ImageOps.invert(imagen)
    return invertir

def voltearImagen (imagen):
    voltear = ImageOps.flip (imagen)
    return voltear

# Función principal

def main ():
    
    #Cargar imagen
    imagen = cargarImagen ("perro.jpg")
    imagen.show()
    
    # Preguntar al usuario que quiere hacer
    
    pregunta = input("¿Quieres invertir o voltear la imagen? ")
    
    # Condición
    
    if pregunta == "invertir":
        invertir = invertirImagen (imagen)
        invertir.show()
    else:
        if pregunta == "voltear":
            voltear = voltearImagen (imagen)
            voltear.show()
        else:
            print ("Esa opción no existe, intenta de nuevo")


main ()