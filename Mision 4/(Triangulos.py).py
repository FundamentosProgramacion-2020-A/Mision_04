# Autor: Miguel Castillo Ordaz
# Programa que escribe el tipo de triángulo de acuerdo a la longitud de los lados del triángulo.

def tipoDeTriangulo(ladoA, ladoB, ladoC):

    if ladoA == ladoB == ladoC:
        
        return ("Equilátero. Los tres lados son iguales.")
    else:
        
        if ladoA == ladoB:

            return ("Isósceles. Dos lados son iguales y el tercero es diferente.")
        else:
            
            if ladoA == ladoC:
                
                return ("Isósceles. Dos lados son iguales y el tercero es diferente.")
            else:

                if ladoB == ladoC:
                    
                    return ("Isósceles. Dos lados son iguales y el tercero es diferente.")
                else:
                    
                    if (ladoA + ladoB) < lado3:
                        
                        return ("Estos lados no corresponden a un triángulo")
                    else:

                        if (ladoA + ladoC) < ladoB:

                            return ("Estos lados no corresponden a un triángulo")
                        else:

                            if (ladoB + ladoC) < ladoA:
                                
                                return ("Estos lados no corresponden a un triángulo")
                            else:
                                
                                return ("Otro. Ninguno de los anteriores.")


def main():

    ladoA = int(input("¿Cuánto mide el lado A de tu triángulo?: "))
    ladoB = int(input("¿Cuánto mide el lado B de tu triángulo?: "))
    ladoC = int(input("¿Cuánto mide el lado C de tu triángulo?: "))
    
    artenVonDreiecken = tipoDeTriangulo(ladoA, ladoB, ladoC)
    print ("Tipo de triángulo:", artenVonDreiecken)

main()