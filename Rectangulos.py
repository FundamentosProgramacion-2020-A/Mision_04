#Kathia Alejandra Cervantes López
#Este programa lee la base y la altura de dos rectángulos y te da el perímetro y área de cada uno.


#Función para calcular el área del rectángulo uno
def calcularAreaRectangulo (base, altura):
    area = base*altura
    return area
    


#Función para calcular el perímetro del rectángulo uno
def calcularPerimetroRectangulo (base, altura):
    perimetroUno = base+altura+base+altura
    return perimetroUno


#Lee las dimensiones de los rectángulos y utiliza las fórmulas definidas en las funciones anteriores para calcular área y perímetro
def main () :
    base = float(input("Escribe la base del primer rectángulo: "))
    altura = float(input("Escribe la altura del primer rectángulo: "))
    areaRectangulo = calcularAreaRectangulo (base, altura)
    print ("El área del rectángulo uno es: ", (areaRectangulo))
    
    perimetroRectangulo = calcularPerimetroRectangulo (base, altura)
    print ("El perímetro del rectángulo uno es: ", (perimetroRectangulo))
    
    base2 = float(input("Escribe la base del segundo rectángulo: "))
    altura2 = float(input("Escribe la altura del segundo rectángulo: "))
    areaRectanguloDos = calcularAreaRectangulo (base2, altura2)
    print ("El área del rectángulo dos es: ", (areaRectanguloDos))
    
    perimetroRectanguloDos = calcularPerimetroRectangulo (base2, altura2)
    print ("El perímetro del rectángulo dos es: ", (perimetroRectanguloDos))
    
    #condición para saber que área es más grande
    if areaRectangulo == areaRectanguloDos:
        print ("El área de los rectángulos es igual")
    else:
        if areaRectangulo > areaRectanguloDos:
            print ("El área del rectángulo uno es mayor que el del rectángulo dos")
        else:
            print ("El área del rectángulo dos es mayor que el del rectángulo uno")

main ()