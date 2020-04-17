#Autor: Samara Andrea Vega
#Cargar una imagen y después preguntar al usuario si desea invertir la imagen o votearla


from PIL import Image, ImageOps   # de la librería PIL, importamos Image

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
    imagen = cargarImagen("cedetec.jpg")
    imagen.show()
    
    preguntaUsuario = input("¿Desea invertir o desea voltear la imagen?")
    if preguntaUsuario == "invertir":
        invertir = convertirInvertir(imagen)
        invertir.show()
    else:
        if preguntaUsuario == "voltear":
            voltear = convertirVoltear(imagen)
            voltear.show()
    
main()