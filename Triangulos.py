#Autor: Elena R.Tovar
#Mision_04: Triángulos
#Leer el valor de cada uno de los lados del triángulo
#Clasificar triángulo de acuerdo a la longitud de sus lados
#Si un triangulo no existe, dar ERROR
#Un triangulo no existe si la suma de dos de sus lados es menor al tercero


def verificarLados(a,b,c):
    if a==0 or b==0 or c==0:
        return "ERROR"
    elif (a+b)>c:
        return "RIGHT"
    elif (a+c)>b:
        return "RIGHT"
    elif (b+c)>a:
        return "RIGHT"
    else:
        return "ERROR"

def clasificarTriangulos(a,b,c):
    if a==b and b==c:
        return "EQUILÁTERO"
    elif a==b or b==c or a==c:
        return "ISÓSCELES"
    else:
        return "OTRO"

def main():
    a= int(input("Ingrese el valor del primer lado: "))
    b= int(input("Ingrese el valor del segundo lado: "))
    c= int(input("Ingrese el valor del tercer lado: "))
    verif=verificarLados(a,b,c)
    if verif=="RIGHT":
        clasif=clasificarTriangulos(a,b,c)
        print("USTED HA INGRESADO UN TRIÁNGULO ",clasif)
    else:
        print ("LOS VALORES QUE HA INGRESADO NO SON VÁLIDOS")
    
main()