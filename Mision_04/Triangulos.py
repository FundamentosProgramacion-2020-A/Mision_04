# Autor: Daniel Rojas, A01376572
# Clasificar un triángulo entre equilátero, isósceles u otro.


def determinarTriangulo(a,b,c):   #Determina si el triángulo existe o no
    suma1 = a+b
    suma2 = b+c
    suma3 = a+c
    if suma1<=c:
        triangulo = 0
    else:
        if suma2<=a:
            triangulo = 0
        else:
            if suma3<=b:
                triangulo = 0
            else:
                triangulo = 1
    return triangulo


def clasificarTriangulo(a,b,c):   #Define si el triángulo es equilátero, isósceles u otro.
    if a==b and b==c:
        tipo = 1
    else:
        if (a==b and b!=c) or (a==c and b!=c) or (b==c and a!=b):
            tipo = 2
        else:
            tipo = 3
    return tipo


def main():  #Función principal
    lado1 = int(input("Teclea la longitud del lado 1: " ))
    lado2 = int(input("Teclea la longitud del lado 2: " ))
    lado3 = int(input("Teclea la longitud del lado 3: " ))
    triangulo = determinarTriangulo(lado1,lado2,lado3)
    if triangulo==0:
        print("Estos lados no corresponden a un triángulo. Vuelva a correr el programa")
    else:
        tipo = clasificarTriangulo(lado1,lado2,lado3)
        if tipo==1:
            print("Se trata de un triángulo EQUILÁTERO")
        else:
            if tipo==2:
                print("Se trata de un triángulo ISÓSCELES")
            else:
                print("Se trata de OTRO tipo de triángulo")

main()