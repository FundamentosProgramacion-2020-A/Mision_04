# Autor: Paloma Argelia Cueto González
# Leer los 3 lados de un triángulo y decir de que tipo es

# Función para saber tipo de triángulo
def definirTriangulo (a, b, c):
    if a == b == c:
        triangulo = "equilatero"
        return triangulo
    else:
        if a == b or a == c or b == c:
            triangulo = "isoceles"
            return triangulo
        else:
            a != b and a != c and b != c
            triangulo = "otro"
            return triangulo
        
                    
def main ():
    
    # Verificar el valor de los triangulos
    a = int (input ("Ingresa el valor del primer lado: "))
    b = int (input ("Ingresa el valor del segundo lado: "))
    c = int (input ("Ingresa el valor del tercer lado: "))
    
    tipoTriangulo = definirTriangulo (a, b, c)
        
    #Condición
    
    if a+b > c and a+c > b and b+c > a:
        print ("Tu triangulo es: ", tipoTriangulo)
    else:
        print ("Estos lados no corresponden a un triangulo")
        
   
main ()