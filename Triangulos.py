#Autor: Valeria Huerta Pedregal
#Leer los valores de cada lado de un triángulo, emitir mensaje correpondiente

def esTriangulo(a,b,c):
    if a + b > c or b + c > a or a + c > b:
        return True
    return False

def esEquilatero(a,b,c):
    if a == b == c:
        return True
    return False

def esIsosceles(a,b,c):
    if a == b or b == c or c == a:
        return True
    return False

def definirTriangulo(a,b,c):
    if esTriangulo(a,b,c) and esEquilatero(a,b,c):
        return "El triángulo es equilatero"
    elif esTriangulo(a,b,c) and esIsosceles(a,b,c):
        return "El triángulo es isosceles"
    elif esTriangulo(a,b,c):
        return "El tríangulo existe pero no es equilatero ni isosceles"
    else:
        return "Estos lados no corresponden a un triángulo"
    

def main():
    a = float(input("Escribe la longitud del primero lado: "))
    b = float(input("Escribe la longitud del segundo lado: ")) 
    c = float(input("Escribe la longitud del tercer lado: "))
    
    t = definirTriangulo(a,b,c)
    print(t)
  
main()