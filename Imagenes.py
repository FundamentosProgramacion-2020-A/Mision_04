#Autor: Brandon Julien Celaya Torres - A01745762
#Descripción: Lee una imagen y pregunta qué operaciones realizar (invertir colores / voltear)

from PIL import Image, ImageOps

def convertirNegativo(imagen):
    imgNegativa = ImageOps.invert(imagen)
    
    return imgNegativa

def voltearImagen(archivo):
    imgVolteada = ImageOps.flip(archivo)
    
    return imgVolteada

def cargarImagen(archivo):
    imagen = Image.open(archivo)
    
    return imagen
    

def main ():
    
    imagen = cargarImagen("brandon.jpg")
    imagen.show()
    
    
    
    respuestaNegativo = input ("¿Quieres convertir a negativo tu imagen? Teclea sí o no: ")
    if respuestaNegativo == "sí":
        negativo = convertirNegativo(imagen)
        negativo.show()
        
        
    respuestaVoltear = input("¿Quieres convertir voltear tu imagen? Teclea sí o no: ")
    if respuestaVoltear == "sí":
        volteado = voltearImagen(imagen)
        volteado.show()

main()