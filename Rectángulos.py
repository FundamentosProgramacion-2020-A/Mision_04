# Autor: Fernando Pérez González
# Lee las dimensiones (base y altura) de dos rectángulos
# Calcular e imprimir el perímetro y área de cada uno.

def calcularAreas(base, altura) : #encuentra el área de rectángulos
    area = base * altura
    return area


def calcularPerimetros(base, altura) : #encuentra el perímetro de los rectángulos
    perimetro = (2*base) + (2*altura)
    return perimetro


def main():
    base = float(input("Escribe la longitud de la base del primer rectángulo: "))
    altura = float(input("Escribe la longitud de la altura del primer rectángulo: "))
    area = calcularAreas(base, altura)
    perimetro = calcularPerimetros(base, altura)
    base2 = float(input("Escribe la longitud de la base del segundo rectángulo: "))
    altura2 = float(input("Escribe la longitud de la altura del segundo rectángulo: "))
    area2 = calcularAreas(base2, altura2)
    perimetro2 = calcularPerimetros(base2, altura2)
    
    print("El área de tu primer rectánculo es de: %.2f" % area)
    print("El área de tu segundo rectánculo es de: %.2f" % area2)
    print("El perímetro de tu primer rectánculo es de: %.2f" % perimetro)
    print("El perímetro de tu segundo rectánculo es de: %.2f" % perimetro2)
    
    if area > area2:
        print ("El primer rectángulo tiene un área mayor") #Se cumplió la condición
    elif area < area2:
        print ("El segundo rectángulo tiene un área mayor")
    else:
        print ("Las áreas de los rectángulos son iguales")
        
    
main()