#Kathia Alejandra Cervantes López
#Este programa da la opción de invertir o voltear una imagen

#Llamar a la libreria
from PIL import Image, ImageOps

#Función que carga a la imagen
def cargarImagen (archivo):
    imagen = Image.open(archivo)
    return imagen


#Función que invierte la imagen
def invertirImagen (imagen):
    imgInvertir = ImageOps.invert (imagen)
    return imgInvertir
    
    
#Función que voltea verticalmente la imagen    
def voltearVertical (imagen) :
    imgVertical = ImageOps.flip (imagen)
    return imgVertical


#Función para llamar las otras funciones
def main():
    imagen = cargarImagen("salchicha.jpg")
    imagen.show()
    
    #Condición para saber que quiere hacer el usuario
    img = input("Quieres voltear o hacer el negativo de tu foto? (únicamente pon 'voltear' o 'negativo' en minúsculas) ")
    if img == "negativo" :
        imagen = invertirImagen (imagen)
        imagen.show()
    else :
        if img == "voltear":
            imagen = voltearVertical(imagen)
            imagen.show()
        else:
            print ("ERROR. Escribe la palabra de acuerdo a los parámetros y vuelvelo a intentar")
    
    
main ()
