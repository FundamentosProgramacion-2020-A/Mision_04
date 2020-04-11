# Autor: Patricio León
# Calcula el área y perimetro de dos rectangulos


# Formula para el área del rectangulo
def calcularArea(base, altura):
    areaFormula = base*altura
    return areaFormula


# Formula para el perimetro del rectangulo
def calcularPerimetro(base, altura):
    areaPerimetro = (base*2) + (altura*2)
    return areaPerimetro

# Programa Inicial
def main():
    altura = float(input("Teclea la altura de tu primer rectangulo: "))
    base = float(input("Teclea la base de tu primer rectangulo: "))
    area1 = calcularArea(base, altura)
    perimetro1 = calcularPerimetro(base, altura)
    
    print ("Área del primer rectangulo: %.f" % (area1))
    print ("Perimetro del primer rectangulo: %.f" % (perimetro1))
    
    
    altura = float(input("Teclea la altura de tu segundo rectangulo: "))
    base = float(input("Teclea la base de tu segundo rectangulo: "))
    area2 = calcularArea(base, altura)
    perimetro2 = calcularPerimetro(base, altura)
    
    print ("Área del segundo rectangulo: %.f" % (area2))
    print ("Perimetro del segundo rectangulo: %.f" % (perimetro2))
    
    if area1 > area2:
        print ("Área del primer rectangulo es mayor a la del segundo")
    else:
        if area1 < area2:
            print ("Área del primer rectangulo es menor a la del segundo")
        else:
            if area1 == area2:
                print ("Área del primer rectangulo y segundo son iguales")
            
        
# Llama a la función principal para resolver el problema 
main ()
