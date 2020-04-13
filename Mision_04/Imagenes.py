# Autor: Daniel Rojas, A01376572
# Invertir o voltear verticalmente una imagen.

from PIL import Image, ImageOps  #Importar funciones de la librería


def cargarImagen(archivo):  #Carga el archivo de imagen
    image = Image.open(archivo)
    return image


def invertirImagen(image):  #Invierte la imagen a negativos
    imgInvert = ImageOps.invert(image)
    return imgInvert

    
def voltearImagen(image):  #Voltea verticalmente la imagen
    imgVolt = ImageOps.flip(image)
    return imgVolt


def main():  #Función principal
    imagen = cargarImagen("Matrix.jpg")
    imagen.show()
    op = str(input("¿Qué operación desea realizar? Invertir o voltear?: "))
    if op == "Invertir":
        img = invertirImagen(imagen)
    else:
        if op == "Voltear":
            img = voltearImagen(imagen)
    img.show()

main()