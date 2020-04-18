from PIL import Image,ImageOps

def cargarImagen(archivo):
    imagen = Image.open(archivo)
    return imagen

def invertirImagen(imagen):
    invertir = ImageOps.invert(imagen)
    return invertir

def voltearImagen(imagen):
    voltear = ImageOps.flip(imagen)
    return voltear
    
def main():
    
    imagen = cargarImagen("imagen.jpg")
    imagen.show()

    img = input("Desea invertir los colores de la imagen o voltear la imagen? ")
    
    if img == "voltear":
        voltear = voltearImagen(imagen)
        voltear.show()
    else:
        if img == "invertir":
            invertir = invertirImagen(imagen)
            invertir.show()
        else:
            print("Error, vuelve a intentar")
        
main()

    
    