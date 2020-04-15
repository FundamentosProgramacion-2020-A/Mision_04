# Autor: Paloma Argelia Cueto González
# Calcular el área y el perimetro de dos rectangulos e imprimir cuál es mayor

# Función para calcular área
def calcularArea (base, altura):
    area = base * altura
    return area

# Función para calcular perimetro
def calcularPerimetro (base, altura):
    perimetro = (base*2) + (altura*2)
    return perimetro

# Programa principal
def main ():
    
# Area y perimetro del primer rectangulo
    altura = int (input("Ingrese la altura del primer rectángulo: "))
    base = int (input("Ingrese la base del primer rectángulo: "))
    
    area1 = calcularArea (base, altura)
    perimetro1 = calcularPerimetro (base, altura)
    
    print ("El área del primer rectángulo es: ", area1)
    print ("El perimetro del primer rectángulo es: ",perimetro1)
    
# Area y perimetro del segundo rectangulo
    altura2 = int (input ("Ingrese la altura del segundo rectángulo: "))
    base2 = int (input( "Ingrese la base del segundo rectángulo: "))
    
    area2 = calcularArea (base2, altura2)
    perimetro2 = calcularPerimetro (base2, altura2)
    
    print ("El área del segundo rectángulo es: ", area2)
    print ("El perimetro del segundo rectángulo es: ",perimetro2)
    
    # Condición para saber que area es más grande
    
    if area1 == area2:
        print ("Las areas son iguales")
    else:
        if area1 >= area2:
            print ("El área del primer rectángulo es más grande")
        else:
            print ("El área del segundo rectángulo es más grande")

main ()