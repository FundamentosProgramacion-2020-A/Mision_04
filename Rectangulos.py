#Autor: Samara Andrea Vega
#Leer las dimensiones de dos rectángulos, posteriormente calcular e imprimir perímetro y área e indicar cuál tiene mayor dimensión

def calcularArea (base, altura):
    area = base * altura
    return area


def calcularPerimetro(base, altura):
    perimetro = base * 2 + altura * 2
    return perimetro
    
    
def main():
    baseUno = int(input("La base del primer rectángulo es: "))
    alturaUno = int(input("La altura del primer rectángulo es: "))
    baseDos = int(input("La base del segundo rectángulo es: "))
    alturaDos = int(input("La altura del segundo rectángulo es: "))
    areaUno = calcularArea(baseUno, alturaUno)
    areaDos = calcularArea(baseDos, alturaDos)
    
    print("El área del primer rectángulo es: ", areaUno)
    print("El área del segundo rectángulo es: ", areaDos)
    
    if areaUno == areaDos:
        print("El área del primer rectángulo es igual al área del segundo rectángulo")
    else:
        if areaUno > areaDos:
            print("El área del primer rectángulo es mayor a la del primer rectángulo")
        else:
            print("El área del segundo rectángulo es mayor que la del primer rectángulo")
    
    perimetroUno = calcularPerimetro(baseUno, alturaUno)
    perimetroDos = calcularPerimetro(baseDos, alturaDos)
    print("El perímetro del primer rectángulo es: ", perimetroUno)
    print("El perímetro del segundo rectángulo es: ", perimetroDos)


main()