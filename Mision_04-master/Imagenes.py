#Autor: Anayansi Alexia Tafoya Soto - A01746781
# Carga de imagen y realización de operaciones.

from PIL import Image, ImageOps
#de la libreria PIL, importamos Image y hacemos operaciones

#Función que carga la imagen desde nuestra computadora
def cargarImagen(archivo):
    imagen = Image.open(archivo)
    return imagen


#Función que calcula el negativo de la imagen
def invertirImagen (imagen):
    imgInv = ImageOps.invert(imagen)
    return imgInv


#Función que voltea la imagen verticalmente
def voltearImagen (imagen):
    imgVoltear = ImageOps.flip(imagen)
    return imgVoltear

def main():
    imagen = cargarImagen ("mundo.jpg")
    imagen.show()
    #Muestra la imagen original
    
    opcion = int (input( "Teclea 1 si deseas invertir la imagen y teclea 2 si deseas voltearla verticalmente: "))
    #Pide la operación que quiere realizar el usuario
    
    if opcion == 1: #Si la opción es 1, se lleva a cabo la función de invertir la imagen
         invertir = invertirImagen (imagen)
         invertir.show()
    else:
        if opcion == 2: #Si la opción es 2, se lleva a cabo la función de voltear verticalmente la imagen
             voltear = voltearImagen (imagen)
             voltear.show()
        else: #No se cumple
            print ("ERROR")
    
#Llamar a función principal
main()