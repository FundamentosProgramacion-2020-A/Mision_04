#Autor: Alondra Miranda
#Imágen

from PIL import Image, ImageOps #de la librería PIL importamos Image

def cargarImagen(archivo): #Carga la imagen desde mi compu
    imagen = Image.open(archivo)
    return imagen


def invertirImagen(imagen): #Invierte la imagen
    inv = ImageOps.invert(imagen)
    return inv
    
    
def voltearImagen(imagen): #Voltea verticalmente ala imagen
    vol = ImageOps.flip(imagen)
    return vol
    

def main():
    imagen = cargarImagen("duda.jpeg")
    imagen.show() #Que se muestre la imagen original
    
    ele = int(input("Si quieres inverir teclea 1 y si quieres voltear teclea 2: ")) #Pregunta al user
    if ele == 1:
        inversion = invertirImagen(imagen)
        inversion.show() #Muestra imagen invertida
    else:
        if ele == 2:
            volteada = voltearImagen(imagen)
            volteada.show() #Muestra imagen volteada
    
main()