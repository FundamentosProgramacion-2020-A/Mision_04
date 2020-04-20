#Kathia Alejandra Cervantes López
#Este programa lee los lados de un triángulo y te dice que tipo de triángulo es

#Función para ver que sí sea un triánguo
def calcularTriangulo (a, b, c,):
    #condición para que sea un triángulo
    if (a + b) < c or (b + c) <a or (c + a) < b :
        return "Estos lados no corresponden a un triángulo"
    

#Función para el triángulo equilatero
def definirTrianguloEquilatero (a, b, c):
    #condicón 
    if a == b and b == c:
        return "Es un triángulo equilátero"


#Función para el triángulo isósceles
def definirTrianguloIsosceles (a,b,c):
    #condición
    if a == b or b == c or c == a:
        return "Es un triángulo isósceles"         
    
    
#Función para llamar a las otras funciones    
def main ():
    #Recibe los valores con los que trabajaremos
    a = float(input("Teclea el lado 'a' del triángulo: "))
    b = float(input("Teclea el lado 'b' del triángulo: "))
    c = float(input("Teclea el lado 'c' del triángulo: "))
    
    #condicón que imprime según el triángulo que se 
    if calcularTriangulo (a, b, c):
        print ("Estos lados no corresponden a un triángulo")
    else:
        if definirTrianguloEquilatero (a, b, c):
            print ("Es un triángulo isósceles")
        else:
            if definirTrianguloIsosceles (a, b, c):
                print ("Es un triángulo isósceles")
            else:
                print ("Es otro tipo de triángulo")            
        
    
main ()