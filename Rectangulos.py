#Autor: Valeria Huerta Pedregal
#Calcular e imprimir área y perímetro de rectángulos

def calcularPerimetro(base, altura):
    perimetro = base*2 + altura*2
    return perimetro

def calcularArea(base, altura):
    area = base*altura
    return area

def main():
    
    base1 = float(input("Ingrese el valor de la base del primer rectángulo: "))
    altura1 = float(input("Ingrese el valor de la altura del primer rectángulo: "))
    
    base2 = float(input("Ingrese el valor de la base del segundo rectángulo: "))
    altura2 = float(input("Ingrese el valor de la altura del segundo rectángulo: "))
    
    totalArea1 = calcularArea(base1,altura1)
    totalPerimetro1 = calcularPerimetro(base1,altura1)
    
    totalArea2 = calcularArea(base2,altura2)
    totalPerimetro2 = calcularPerimetro(base2,altura2)
    
    print("")
    print("El área total del primer rectángulo es de",totalArea1,"unidades")
    print("El perímetro total del primer rectángulo es de",totalPerimetro1,"unidades")
    print("El área total del segundo rectángulo es de",totalArea2,"unidades")
    print("El perímetro total del segundo rectángulo es de",totalPerimetro2,"unidades")
    print("")
    
    if totalArea1 > totalArea2:
        print ("El primer rectángulo tiene mayor área que el segundo.")
    else:   
        if totalArea1 < totalArea2:
            print ("El segundo rectángulo tiene mayor área que el primero.")
        else:
            print("Los rectángulos tienen el mismo área")

main()
