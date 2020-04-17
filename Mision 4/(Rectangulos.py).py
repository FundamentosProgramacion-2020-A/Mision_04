# Autor: Miguel Castillo Ordaz
# Programa que calcula perímetro y área de dos rectángulos y compara.



def calcularArea(base, altura):

    areaFormula = base*altura

    return areaFormula

def calcularPerimetro(base, altura):
    
    areaPerimetro = 2*(base + altura)
    return areaPerimetro

def main():

    altura = float(input("¿Qué altura tiene tu primer rectángulo? "))

    base = float(input("¿Cuál es la base que tiene tu primer rectángulo? "))

    areaA = calcularArea(base, altura)
    
    perimetroA = calcularPerimetro(base, altura)

    print ("El área de tu primer rectángulo es: %.f" % (areaA))

    print ("El perímetro de tu primer rectángulo es: %.f" % (perimetroA))

    altura = float(input("¿Qué altura tiene tu primer rectángulo? "))

    base = float(input("¿Cuál es la base que tiene tu primer rectángulo? "))

    areaB = calcularArea(base, altura)

    perimetroB = calcularPerimetro(base, altura)

    print ("El área de tu primer rectángulo es: %.f" % (areaB))

    print ("El perímetro de tu primer rectangulo es: %.f" % (perimetroB))
    if areaA > areaB:

        print ("El área del primer rectángulo es mayor a la del segundo.")

    else:
        if areaA < areaB:

            print ("El área del primer rectángulo es menor a la del segundo.")

        else:
            if areaA == areaB:

                print ("El área del primer rectángulo y segundo son iguales.")

main ()