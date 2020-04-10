# Autor: Michelle Ojeda Manjarrez
# Invertir y voltear verticalmente una imagen


#Importamos Image y ImageOps de la libereria PIL
from PIL import Image, ImageOps


#Definimos función cargar imagen
def cargarImagen (archivo):
    imagen = Image.open (archivo)
    return imagen


#Definimos función invertir imagen
def invertirImagen (imagen):
    invertir =  ImageOps.invert (imagen)
    return invertir


#Definimos función voltear verticalmente la imagen
def voltearImagen (imagen):
    voltear =  ImageOps.flip (imagen)
    return voltear


#Función principal
def main ():
    
    #Se carga la imagen 
    imagen = cargarImagen ("NuevaYork.jpg")
    imagen.show()
    
    img = input ("¿Quieres invertir o voltear la imagen?: ")
    
    #Condicionante
    if img == "invertir":
         invertir = invertirImagen (imagen)
         invertir.show()
    else:
        if img == "voltear":
            voltear = voltearImagen (imagen)
            voltear.show()
        else:
            print ("Error: Vuelve a intentarlo")
    
main ()