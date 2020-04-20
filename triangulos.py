#Roberto Sobrado
#Clasificar triangulos

def validarTriangulo(lado1, lado2, lado3):
    total = lado1 + lado2
    if total >= lado3:
        return True
    
    return False

def clasificarTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return ("Equilátero")
    elif lado1 == lado2 and lado2 != lado3:
        return ("Isósceles")
    elif lado3 == lado2 and lado3 != lado1:
        return ("Isósceles")
    elif lado1 == lado3 and lado2 != lado1:
        return ("Isósceles")
    else:
        return ("Obtuso")
    
def main ():
    lado1 = int(input("¿Cuánto mide un lado?"))
    lado2 = int(input("¿Cuánto mide otro lado?"))
    lado3 = int(input("¿Cuánto mide el último lado?"))
    
    validar = validarTriangulo(lado1, lado2, lado3)
    
    if validar:
        triangulo = clasificarTriangulo(lado1, lado2, lado3)
        print (triangulo)  
    else:
        print ("estos lados no corresponden a un triángulo")
        
main()