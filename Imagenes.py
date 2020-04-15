#Autor: Guadalupe Iveth Serrano Hernández A01375932
#Descripción: Carga una imagen y pregunta al usuario si quiere
#invertir o voltear verticalmente la imagen.

from PIL import Image, ImageOps

def cargarImagen(archivo):
    imagen = Image.open(archivo)
    return imagen


def convertirInvertir(imagen):
    invertir = ImageOps.invert(imagen)
    return invertir
    
    
def convertirVoltear(imagen):
    voltear = ImageOps.flip(imagen)
    return voltear


def main():
    imagen = cargarImagen("problema2.jpg")
    imagen.show()
    
    preguntaUsuario = input("¿Desea invertir o voltear la imagen? ")
    if preguntaUsuario == "invertir":
        invertir = convertirInvertir(imagen)
        invertir.show()
    else:
        if preguntaUsuario == "voltear":
            voltear = convertirVoltear(imagen)
            voltear.show()
    
main()