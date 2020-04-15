#Autor: Guadalupe Iveth Serrano Hernández A01375932
#Descripción: Leer las dimensiones de dos rectángulos, calcular e
#imprimir el perímetro y área e indicar que rectangulo tiene mayor área.

def calcularArea (base, altura):
    area = base*altura
    return area


def calcularPerimetro(base, altura):
    perimetro = base*2+altura*2
    return perimetro
    
    
def main():
    baseUno = int(input("Base del primer rectangulo: "))
    alturaUno = int(input("Altura del primer rectangulo: "))
    baseDos = int(input("Base del segundo rectangulo: "))
    alturaDos = int(input("Altura del segundo rectangulo: "))
    areaUno = calcularArea(baseUno, alturaUno)
    areaDos = calcularArea(baseDos, alturaDos)
    print("El área del primer rectangulo es: ", areaUno)
    print("El área del segundo rectangulo es: ", areaDos)
    
    if areaUno == areaDos:
        print("El área del primer rectangulo es igual al área del segundo rectangulo")
    else:
        if areaUno > areaDos:
            print("El área del primer rectangulo es mayor que la del primer rectangulo")
        else:
            print("El área del segundo rectangulo es mayor que la del primer rectangulo")
    
    perimetroUno = calcularPerimetro(baseUno, alturaUno)
    perimetroDos = calcularPerimetro(baseDos, alturaDos)
    print("El perímetro del primer rectangulo es: ", perimetroUno)
    print("El perímetro del segundo rectangulo es: ", perimetroDos)


main()