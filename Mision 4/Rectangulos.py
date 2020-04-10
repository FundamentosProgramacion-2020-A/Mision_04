# Mariana Mejía Béjar
# Calcula área y perímetro de dos rectángulos, y determina el de mayor área


# Guarda la fórmula para calcular el área
def calcularArea(base, altura):
    area = base * altura
    return area


# Guarda la fórmula para calcular el perímetro
def calcularPerimetro(base,altura):
    perimetro = 2*base + 2*altura
    return perimetro


# Función principal. Le pregunta al usuario las medidas de los rectángulos y procede a mencionarle
# las áreas y los perímetros respectivos. Después indica cuál tiene la mayor área o si son iguales.
def main():
    
    base1 = int(input("Base del primer rectángulo: "))
    altura1 = int(input("Altura del primer rectángulo: "))
    base2 = int(input("Base del segundo rectángulo: "))
    altura2 = int(input("Base del segundo rectángulo: "))

    area1 = calcularArea(base1,altura1)
    perimetro1 = calcularPerimetro(base1,altura1)
    area2 = calcularArea(base2,altura2)
    perimetro2 = calcularPerimetro(base2,altura2)

    print("El área del primer rectángulo es de",area1,"unidades cuadradas, y su perímetro es de",perimetro1,"unidades.")
    print("El área del segundo rectángulo es de",area2,"unidades cuadradas, y su perímetro es de",perimetro2,"unidades.")

    if area1 > area2:
        print("El rectángulo con mayor área es: el primero")
    else:
        if area1 < area2:
            print("El rectángulo con mayor área es: el segundo")
        else:
            print ("El área de ambos rectángulos es igual")


main() 