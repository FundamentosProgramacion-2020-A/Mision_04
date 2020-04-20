#Roberto Sobrado
#Calcular area y perimetro con dimensiones de dos tringulos

def calcularPerimetro1(base1, altura1):
    perimetro = (2*base1) + (2*altura1)
    return perimetro

def calcularPerimetro2(base2, altura2):
    perimetro = (2*base2) + (2*altura2)
    return perimetro
def calcularAreaUno(base1, altura1):
    area = (base1*altura1)
    return area
    
def calcularAreaDos(base2, altura2):
    area = (base2*altura2)
    return area

def diferenciarArea(area1, area2): #saber cual perimetro es mayor
    if area1 > area2:
        return "El área del primer rectangulo es el mayor."
    elif area1 < area2:
        return "El área del segundo rectangulo es el mayor." 
    else:
        return "El área de ambos rectangulos es el mismo."

def main(): #programa principal
    base1 = int(input("¿Cuánto mide la base del primer rectangulo?"))
    altura1 = int(input("Cuánto mide la altura del primer rectangulo?"))
    base2 = int(input("¿Cuánto mide la base del segundo rectangulo?"))
    altura2 = int(input("Cuánto mide la altura del segundo rectangulo?"))
    
    perimetro1 = calcularPerimetro1(base1, altura1)
    print ("El perímetro del primer recángulo mide %.2fm." % (perimetro1))
    
    perimetro2 = calcularPerimetro2(base2, altura2)
    print ("El perímetro del segundo recángulo mide %.2fm." % (perimetro2))
    
    area1 = calcularAreaUno(base1, altura2)
    area2 = calcularAreaDos(base2, altura2)
    print ("El área del primer rectangulo mide %.2fm2." % (area1))
    print ("El área del segundo rectangulo mide %.2fm2." % (area2))   
    
    area = diferenciarArea(area1, area2)
    print (area)
    
    
main()