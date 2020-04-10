# Autor: Michelle Ojeda Manjarrez
# Calcular el perímetro y el área de dos rectángulos

#Definir función calcular Área
def calcularArea (base, altura):
    area = base * altura
    return area


#Definir función calcular Perímetro
def calcularPerimetro (base, altura):
    perimetro = (base*2) + (altura*2)
    return perimetro


#Programa inicial
def main ():
    
    #Se saca el área y el perímetro del rectángulo 1
    altura = float (input ("Escribe la altura del rectangulo 1: "))
    base = float (input ("Escribe la base del rectangulo 1: "))
    
    areaUno = calcularArea (base, altura)
    print ("El área del rectángulo 1 es: %.02f" % areaUno)
    
    perimetroUno = calcularPerimetro (base, altura)
    print ("El perímetro del rectángulo 1 es: %.02f" % perimetroUno)
    
    
    #Se saca el área y el perímetro del rectángulo 2
    altura = float (input ("Escribe la altura del rectangulo 2: "))
    base = float (input ("Escribe la base del rectangulo 2: "))
    
    areaDos = calcularArea (base, altura)
    print ("El área del rectángulo 1 es: %.02f" % areaDos)
    
    perimetroDos = calcularPerimetro (base, altura)
    print ("El perímetro del rectángulo 1 es: %.02f" % perimetroDos)
    

    #Condicionante
    if areaUno == areaDos:
        print ("Las areas son iguales")
    else:
        if areaUno <= areaDos:
            print ("El area del triangulo 1 tiene menor area que el triangulo 2")
        else:
            print ("El area del triangulo 2 tiene mayor area que el triangulo 1")
            
    
main()