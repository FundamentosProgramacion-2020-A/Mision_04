#Autor: Alondra Miranda
#Area y Perímetro de 2 rectángulos

def calcularArea(b,h):
    area=b*h
    return area
    
def calcularPeri(b,h):
    peri=(b*2)+(h*2)
    return peri


def main():
    rect1ba = int(input("¿Cuál es la base del Rectángulo 1?: "))
    rect1al = int(input("¿Cuál es la altura del Rectángulo 1?: "))
    rect2ba = int(input("¿Cuál es la base del Rectángulo 2?: "))
    rect2al = int(input("¿Cuál es la altura del Rectángulo 2?: "))
    
    area1= calcularArea(rect1ba, rect1al)
    print("Area del Rectángulo 1: ", area1)
    area2=calcularArea(rect2ba, rect2al)
    print("Area del Rectángulo 2: ", area2)
    
    peri1= calcularPeri(rect1ba, rect1al)
    print("Perímetro del Rectángulo 1: ", peri1)
    peri2=calcularPeri(rect2ba, rect2al)
    print("Perímetro del Rectángulo 2: ", peri2)
    
    if area1>area2:
        print("El rectángulo 1 es mayor")
    else:
        print("El rectángulo 2 es mayor")
        
main()