# Autor : Sharone Márquez, A01746940 
# Escribir un programa que lea el valor de los lados de un triangulo y definir que tipo es


#Programa principal
def main ():
    lado1= int(input ("Escibe el valor del primer lado: "))
    lado2= int(input ("Escribe el valor del segundo lado: "))
    lado3= int(input ("Escribe el valor del terce lado: "))
    
    #Condición para saber si el triangulo existe
    if (lado1+lado2) < lado3:
        print ("Estos lados no corresponden a un triángulo")
     
    #Condición para saber que tipo de triangulo es
    if lado1 == lado2 == lado3:
            print ("Es un triángulo equilátero") 
    else:
        if lado1 == lado2:              
            print ("Es un triángulo isóceles")
        else:
            if lado2 == lado3:
                print ("Es un triángulo isóceles")
            else:    
                print ("Es otro tipo de triángulo")
                
                
main()