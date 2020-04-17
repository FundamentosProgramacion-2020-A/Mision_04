# Paulina Mendoza Iglesias
# El programa indica el tipo de triángulo de acuerdo a su longitud
    

def main ():
    
    ladoA = int(input("Teclea el valor 1: "))
    ladoB = int(input("Teclea el valor 2: "))
    ladoC = int(input("Teclea el valor 3: "))
    
        
    
    if ladoA == ladoB and ladoB == ladoC:
        print ("El triángulo es equilátero")
        
    elif ladoA == ladoB and ladoB != ladoC:
        print ("El triángulo es isósceles")
        
    elif ladoA != ladoB and ladoB == ladoC:
        print ("El triángulo es isósceles")
        
    elif ladoA == ladoC and ladoB != ladoC:
        print("El trángulo es isósceles")
        
     
    else:
        print ("Otro")
        
        
    if (ladoA + ladoB) < ladoC:
        print ("No existe el triángulo")
        
    elif (ladoB +ladoC) < ladoA:
        print ("No existe el triángulo")
        
    elif (ladoA + ladoC) <  ladoB:
        print ("No existe el triángulo")    
    
        
#Llamada a main ()
main()
