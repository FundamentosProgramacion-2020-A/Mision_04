# Mariana Mejía Béjar
# Determina si un triángulo existe y el tipo de triángulo, de acuerdo a los lados brindados por el usuario


# Define la función principal. Le pregunta al usuario las medidas, determina si existe el triángulo
# y en caso de que sí, menciona qué tipo de triángulo es
def main():
    lado1 = int(input("Medida del primer lado: "))
    lado2 = int(input("Medida del segundo lado: "))
    lado3 = int(input("Medida del tercer lado: "))
    
    if (lado1+lado2) < lado3:
        print("Estas medidas no corresponden a un triángulo")
    else:
        if (lado2+lado3) < lado1:
            print("Estas medidas no corresponden a un triángulo")
        else:
            if (lado1+lado3) < lado2:
                print("Estas medidas no corresponden a un triángulo")
            else:
    
                
                if lado1==lado2==lado3:
                    print("Es un triángulo equilátero")
                else:
                    if lado1==lado2:
                        print("Es un triángulo isósceles")
                    else:
                        if lado1==lado3:
                            print("Es un triángulo isósceles")
                        else:
                            if lado2==lado3:
                                print("Es un triángulo isósceles")
                            else:
                                print("No es un triángulo equilátero o isósceles")
                    
                    
main()
                    
                    
                    
            
        