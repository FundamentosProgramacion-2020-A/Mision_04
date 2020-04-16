#Autor: Anayansi Alexia Tafoya Soto - A01746781
#Calculo de área y perimetro de dos rectangulos


def calcularArea (base, altura):
    #Calcula el área de ambos rectangulos
    area = base * altura
    return area

def calcularPerimetro (base, altura):
    #Calcula el perimetro de ambos rectangulos
    perimetro = (2*base) + (2*altura)
    return perimetro



def main():
    base1 = int (input ("Teclea la base del rectangulo 1: "))
    altura1 = int (input ("Teclea la altura del rectangulo 1 : "))
    
    base2 = int (input ("Teclea la base del rectangulo 2: "))
    altura2 = int (input ("Teclea la altura del rectangulo 2: "))
    
    area1 = calcularArea (base1, altura1)
    print ("El área del rectangulo 1 es de: ", area1)
                  
    area2 = calcularArea (base2, altura2)
    print ("El área del rectangulo 2 es de: ", area2)
    
    perimetro1 = calcularPerimetro (base1, altura1)
    print ("El perimetro del rectangulo 1 es de: ", perimetro1)
                  
    perimetro2 = calcularPerimetro (base2, altura2)
    print ("El perimetro del rectangulo 2 es de: ", perimetro2)
    
    if area1>area2:
        print ("El área del rectangulo 1 es mayor al rectangulo 2")
    else:
        if area1<area2:
            print ("El área del rectangulo 2 es mayor al rectangulo 1")
        else:
            if area1==area2:
                print ("Ambas áreas son iguales")
            
#Llamar a función principal
main()