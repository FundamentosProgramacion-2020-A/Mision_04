#Autor: Anayansi Alexia Tafoya Soto - A01746781
# Leer el valor de cada triangulo y catalogarlo por tipo.


def main():
    lado1 = int (input ("Teclea el primer lado del triangulo: "))
    lado2 = int (input ("Teclea el segundo lado del triangulo: "))
    lado3 = int (input ("Teclea el tercer lado del triangulo: "))
     
    if lado1 == lado2 == lado3:
        print ("Es un triángulo equilátero")
    elif lado1 == lado2 !=lado3 or lado1 != lado2 == lado3:
        print ("Es un triángulo isóceles")
    else:
        if lado1 != lado2 != lado3:
            print ("Estos lados no corresponden a un triángulo")
        
#Llamar a función principal
main()