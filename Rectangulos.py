# Paulina Mendoza Iglesias
# El programa calcúla áreas de rectángulos

def calcularArea(base, altura):
    area = base * altura
    return area

def calcularPerimetro(base, altura):
    perimetro = (base*2) + (altura*2)
    return perimetro


def main ():
    
    base = int(input("Teclea la base del rectángulo 1: "))
    altura = int(input("Teclea la altura del rectángulo 1: "))
    areaUno = calcularArea (base, altura)
    perimetroUno = calcularPerimetro (base, altura)
    
    base = int(input("Teclea la base del rectángulo 2: "))
    altura = int(input("Teclea la altura del rectángulo 2: "))
    areaDos = calcularArea (base, altura)
    perimetroDos = calcularPerimetro (base, altura)
    
    
    print ("Área del rectángulo 1: %d" % (areaUno))
    print ("Área del rectángulo 2: %d" % (areaDos))
    
    print ("Perímetro del rectángulo 1: %d" % (perimetroUno))
    print ("Perímetro del rectángulo 2: %d" % (perimetroDos))
    
    if areaUno > areaDos:
        print ("El rectángulo 1 tiene un área mayor")
        
    elif areaUno == areaDos:
        print ("Las áreas son iguales")
        
    else:
        print("El rectángulo 2 tiene área mayor")
        
        
          
        
#Llamada a main ()
main()
