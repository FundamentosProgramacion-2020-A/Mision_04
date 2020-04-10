# Mariana Mejía Béjar
# Invierte o voltea verticalmente una imagen

from PIL import Image, ImageOps


# Carga la imagen que será utilizada para el ejercicio
def cargarImagen(archivo):
    imagen = Image.open(archivo)
    return imagen


# Define la función principal en donde se muestra la imagen y se le brinda al usuario el menú con las
# opciones para que elija qué quiere hacerle. Después, procede a ejecutar la opción que el usuario
# seleccionó.
def main():
    imagen = cargarImagen("prueba.jpeg")
    imagen.show()
   
   #Menu
    print("------MENU------")
    print("a. Invertir")
    print("b. Voltear verticalmente")
    seleccion = input("Elige una opción: ")

    if seleccion=="a":
        imagen = ImageOps.invert(imagen)
    else:
        if seleccion=="b":
            imagen = ImageOps.flip(imagen)

    imagen.show()


main()