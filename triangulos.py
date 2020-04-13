#Autor: Alondra Miranda A01746742
#Ejercicio 4: Trángulos de la Misión 4

def main():
    lado1 = int(input("Medida del lado 1: "))
    lado2 = int(input("Medida del lado 2: "))
    lado3 = int(input("Medida del lado 3: "))
    
    if lado1 == lado2 == lado3:
        print("Es triánguo Equilátero")
    else:
        if lado1 != lado2 != lado3:
            print("Estos lados no corresponden a un triángulo")
        else:
            if lado1 == lado2 != lado3 or lado1 != lado2 == lado3:
                print("Es un triángulo isósceles")
        
main()