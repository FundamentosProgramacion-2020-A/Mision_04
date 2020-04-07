#Autor: Brandon Julien Celaya Torres - A01745762
#Descripción: Calcula el área y perímetro de dos rectángulos, las imprime y dice cuál tiene área mayor



def calcularArea (base, altura):
    area = base*altura
    
    return area
    
def calcularPerimetro (base, altura):
    perimetro = 2*base + 2*altura
    return perimetro

def main ():
    
    base = int(input("Introduce la base del rectángulo: "))
    altura = int(input("Introduce la altura del rectángulo: "))
    area1 = calcularArea(base, altura)
    perimetro1 = calcularPerimetro(base,altura)
    
    base = int(input("Introduce la base del rectángulo: "))
    altura = int(input("Introduce la altura del rectángulo: "))
    area2 = calcularArea(base, altura)
    perimetro2 = calcularPerimetro(base,altura)
    
    
    print ("""
            Área del primer rectángulo: %d
            Área del segundo rectángulo: %d """ % (area1, area2))
    
    print ("""
            Perímetro del primer rectángulo: %d
            Perímetro del segundo rectángulo: %d """ % (perimetro1, perimetro2))
    
    if area1 > area2:
        print("""
                    El primer rectángulo tiene área más grande que el segundo""")
    else:
        if area1 == area2:
            print("""
                    Las áreas son iguales""")
        else:
            print ("""
                    El segundo triángulo tiene área más grande que el primero""")
    
    
    
    
    
main()