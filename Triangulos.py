#Autor: Michelle Ojeda Manjarrez
# Calcular si existe el triángulo y que tipo de triángulo es

#Función principal
def main ():
    
    ladoA = float (input ("Teclear el valor del lado A: "))
    ladoB = float (input ("Teclear el valor del lado B: "))
    ladoC = float (input ("Teclear el valor del lado C: "))
    
# Condicionante para  ver si es un triángulo

    if (ladoA + ladoB)< ladoC:
        print ("Estos lados no corresponden a un triángulo")
    else:
        if (ladoB + ladoC) < ladoA:
            print ("Estos lados no corresponden a un triángulo")
        else:
            if (ladoC + ladoA) < ladoB:
                print ("Estos lados no corresponden a un triángulo")

# Condicionante para  ver que tipo de triángulo es
        
    if ladoA == ladoB == ladoC:
            print ("Es un triángulo Equiilátero") 
    else:
        if ladoA == ladoB:              
            print ("Es un triángulo Isóceles")
        else:
            if ladoB == ladoC:
                print ("Es un triángulo Isóceles")
            else:    
                print ("Es otro tipo de triángulo")

            
main()