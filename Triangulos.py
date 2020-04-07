#Autor: Brandon Julien Celaya Torres - A01745762
#Descripción: Lee lados de un triángulo y lo calsifica si es que existe





def main():
    
    lado1 = int(input("Introduce el primer lado del triángulo: "))
    lado2 = int(input("Introduce el segundo lado del triángulo: "))
    lado3 = int(input("Introduce el tercer lado del triángulo: "))
    
    
    
    if (lado1+lado2) < lado3:
        print("No existe tal triángulo")
    else:
        if (lado1+lado3) < lado2:
            print("No existe tal triángulo")
        else:
            if (lado2+lado3) < lado1:
                print("No existe tal triángulo")
            else:
                
                
                
                if lado1 == lado2 == lado3:
                    print("Es un triángulo equilátero")
                else:
                    if lado1 == lado2 != lado3:
                        print("Es un triángulo isósceles")
                    else:
                        if lado1 != lado2 == lado3:
                            print ("Es un triángulo isósceles")
                        else:
                            if lado1 == lado3 != lado2:
                                print ("Es un triángulo isósceles")
                            else:
                                print("No es ni equilátero ni isósceles")
                    

main()