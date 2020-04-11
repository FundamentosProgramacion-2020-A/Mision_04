# Autor: Patricio León
# Escribe un programa que diga que tipo de triangulo es o si no existe


# Definir que tipo de triangulo es de acuerdo a los lados
def definirLado(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Tu triangulo es equilátero, los tres lados son iguales"
    else:
        if lado1 == lado2:
            return "Tu triangulo es isósceles, dos lados son iguales y el tercero es diferente"
        else:
            if lado1 == lado3:
                return "Tu triangulo es isósceles, dos lados son iguales y el tercero es diferente"
            else:
                if lado2 == lado3:
                    return "Tu triangulo es isósceles, dos lados son iguales y el tercero es diferente"
                else:
                    if (lado1 + lado2) < lado3:
                        return "Estos lados no corresponden a un triángulo"
                    else:
                        if (lado1 + lado3) < lado2:
                            return "Estos lados no corresponden a un triángulo"
                        else:
                            if (lado2 + lado3) < lado1:
                                return "Estos lados no corresponden a un triángulo"
                            else:
                                return "Es otro tipo de triangulo"

                    
                            
                                
# Dónde se terminará que tipo de triangulo es
def main():
    lado1 = int(input("¿Cuánto mide el primer lado de tu triangulo?: "))
    lado2 = int(input("¿Cuánto mide el segundo lado de tu triangulo?: "))
    lado3 = int(input("¿Cuánto mide el tercer lado de tu triangulo?: "))
    
    triangulo = definirLado(lado1, lado2, lado3)
    print ("Respuesta: ", triangulo)
    
                                    
# Llama a la función principal para resolver el problema
main()
