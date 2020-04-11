# Sharone Márquez, A01746940
# Escribir un programa que cargue una imagen y preguntar al usuario qué operación se realizará

from PIL import Image, ImageOps

#Función para cargar la imagen
def cargarImagen(archivo):
    imagen = Image.open(archivo)
    return imagen
    
#Programa inicial  
def main():
    imagen= cargarImagen("mickey mouse.jpg")
    imagen.show()
    
    
    Pregunta= input("Escriba 1 para invertir la imagen o 2 para voltear la imagen: ")
    
    #Condiciones
    if Pregunta == "1":
        imagen= ImageOps.invert(imagen)
    else:
        if Pregunta == "2":
            imagen= ImageOps.flip(imagen)
            
    imagen.show()
    
    
main()