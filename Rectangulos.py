#José Manuel Rivera Sosapavón
#Rectangulos
#Escribe un programa que lea las dimensiones (base y altura) de dos rectángulos y que calcule e imprima el perímetro y área de cada uno.
#• Escribe una sola función que reciba las dimensiones del rectángulo y regrese el área.
#• Escribe una sola función que reciba las dimensiones del rectángulo y regrese el perímetro.
#• El programa debe indicar cuál rectángulo tiene mayor área (primero o segundo), o si las áreas son iguales.


def calcularArea(base,altura):
    area = base*altura
    return area


def calcularPerimetro(base,altura):
    perimetro = (base*2) + (altura*2)
    return perimetro

def main ():
    
    b1 = float(input("Tamaño de la base en cm: "))
    h1 = float(input("Tamaño de la altura en cm: "))
    
    b2 = float(input("Tamaño de la base en cm: "))
    h2 = float(input("Tamaño de la altura en cm: "))
    
    a1 = calcularArea(b1,h1)
    p1 = calcularPerimetro(b1,h1)
    
    a2 = calcularArea(b2,h2)
    p2 = calcularPerimetro(b2,h2)
    
    print ("Area del primer rectangulo: %.2f cm cuadrados" % (a1))
    print ("Base del primer rectangulo: %.2f cm " % (b1))
    
    print ("Area del segundo rectangulo: %.2f cm cuadrados" % (a2))
    print ("Base del segundo rectangulo: %.2f cm " % (b2))
    
    if a1>a2:
        print ("El area del primer rectangulo (%.2f) es mayor a la del segundo (%.2f)" % (a1,a2))
        
    if a2>a1:
        print ("El area del segundo rectangulo (%.2f) es mayor a la del primer (%.2f)" % (a2,a1))
        
    if a2 == a1:
        print ("El area de los rectangulos son iguales")
    

main()
    
    
