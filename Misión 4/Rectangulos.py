# Sharone Márquez, A017469400
# Escribir un programa que lea la base y altura de dos rectángulos y calcule e imprima el área y perímetro.

#Función para calcular el área
def calcularArea(base, altura):
    area= (base*altura)/2
    return area


#Función paara calcular el perímetro
def calcularPerimetro(base, altura):
    perimetro= (base*2) + (altura*2)
    return perimetro


#Programa inicial
def main():
    a1= int(input("Ingrese la altura del primer rectángulo: "))
    b1= int(input("Ingrese la base del primer rectángulo: "))
    a2= int(input("Ingrese la altura del segundo rectángulo: "))
    b2= int(input("Ingrese la base del segundo rectángulo: "))
    
    area1= calcularArea(a1,b1)
    perimetro1= calcularPerimetro(a1,b1)
    area2= calcularArea(a2,b2)
    perimetro2= calcularPerimetro(a2,b2)
    
    print("El área del primer rectángulo es:", area1)
    print("El perímetro del primer rectángulo es:", perimetro1)
    print("El área del segundo rectángulo es:", area2)
    print("El perímetro del segundo rectángulo es:", perimetro2)
    
    #Condiciones
    if area1 > area2:
        print("El rectángulo con mayor área es: el primer rectángulo")
        
    else:
        if area1 < area2:
            print("El rectángulo con mayor área es: el segundo rectángulo")
            
        else:
            print("El área de ambos rectangulos es igual")
            

main()