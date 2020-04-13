# Autor: Daniel Rojas, A01376572
# Calcular perímetro y área de 2 rectángulos, así como indicar cual tiene mayor área.


def calcularPerimetro(base,altura):   #Calcula el perímetro a partir de la base y la altura.
    p = base + altura + base + altura
    return p


def calcularArea(base,altura):   #Calcula el área a partir de la base y la altura.
    a = base*altura
    return a


def escogerMayor(a1,a2):  #Selecciona cuál rectángulo tiene un área mayor o si ambos son iguales
    if a1>a2:
        mayor = 1
    else:
        if a1<a2:
            mayor = 2
        else:
            mayor = 0
    return mayor

def main():  #Función principal
    b1 = int(input("Teclea la base del primer rectángulo: "))
    h1 = int(input("Teclea la altura del primer rectángulo: "))
    b2 = int(input("""
Teclea la base del segundo rectángulo: """))
    h2 = int(input("Teclea la altura del segundo rectángulo: "))
    perimetro1 = calcularPerimetro(b1,h1)
    area1 = calcularArea(b1,h1)
    perimetro2 = calcularPerimetro(b2,h2)
    area2 = calcularArea(b2,h2)
    mayor = escogerMayor(area1,area2)
    print ("""
El perímetro del primer rectángulo es:""",perimetro1)
    print ("El área del primer rectángulo es:",area1)
    print ("""
El perímetro del segundo rectángulo es:""",perimetro2)
    print ("El área del segundo rectángulo es:",area2)
    if mayor == 1:
        print ("El primer rectángulo es el de mayor área")
    else:
        if mayor == 2:
            print ("""
El segundo rectángulo es el de mayor área""")
        else:
            print ("El área de ambos rectángulos es igual")
    

main()