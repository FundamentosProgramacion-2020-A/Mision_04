#Roberto Sobrado
#

from PIL import Image, ImageOps

def cargarImagen(archivo): #cargar imagen
    imagen = Image.open(archivo)
    return imagen

def convertirImagenNegativo(imagen): #convierte la imagen a negativo
    negativo = ImageOps.invert(imagen)
    return negativo
    
def voltearImagen(imagen):
    volteo = ImageOps.flip(imagen)
    return volteo

def main():
    decidir = (input("Voltear o negativo de su imagen"))
    
    imagen = cargarImagen("herodoto.jpg")
    imagen.show()
        
    if decidir == "negativo":
        negativo = convertirImagenNegativo(imagen)
        negativo.show()
    else:
        if decidir == "voltear":
            voltear = voltearImagen(imagen)
            voltear.show()
        else:
            print ("error")
    
    
main()

