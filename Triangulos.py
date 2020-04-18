#Autor: Michelle Ojeda Manjarrez
# Calcular si existe el triángulo y que tipo de triángulo es


#Función para saber si es un triángulo
def calcularTriangulo (a, b, c):
    if (a + b)< c:
        return "Estos lados no corresponden a un triángulo"
    else:
        if (b + c) < a:
            return "Estos lados no corresponden a un triángulo"
        else:
            if (c + a) < b:
                return "Estos lados no corresponden a un triángulo"
            
            
#Función para saber si es un triángulo equilátero
def calcularTrianguloEquilatero (a, b, c):
    
    if a == b and b == c:
        return "Es un triángulo Equilátero"
    

#Función para saber si es un triángulo isóceles
def calcularTrianguloIsoceles (a, b, c):
    if a == b:
         return "Es un triángulo Isóceles"
    else:
        if b == c:
            return "Es un triángulo Isóceles"
        else:
            if c == a:
                return "Es un triángulo Isóceles"
            
                
#Función principal
def main ():
    
    a = float (input ("Teclear el valor del lado A: "))
    b = float (input ("Teclear el valor del lado B: "))
    c = float (input ("Teclear el valor del lado C: "))
    
    
#Condicionante   
    if calcularTriangulo ( a, b, c):
        print ("Estos lados no corresponden a un triángulo")
    else:
        if calcularTrianguloEquilatero (a, b, c):
            print ("Es un triángulo Equilátero")
        else:
            if calcularTrianguloIsoceles (a,b,c):
                print ("Es un triángulo Isóceles")
            else:
                print ("Es otro tipo de triángulo")
   
            
main()