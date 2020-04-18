#Autor: Elena R.Tovar A01376318
#Misión 4 - Áreas de rectángulos

def compararAreas(a1,a2):  #Compara las áreas
    if a1==a2:
        return "Ambas áreas son iguales"
    elif a1>a2:
        return "El área del primer rectángulo es mayor"
    else:
        return "El área del segundo rectángulo es mayor"

def calculaPerimetro(b,h): #Calcula el perimetro
    p=(b*2)+(h*2)
    return p

def obtenerArea(b,h): #Calcula las áreas
    a=b*h
    return a

def main():
   b1= int(input("Ingrese el valor de la base del primer rectángulo en centímetros: "))
   h1= int(input("Ingrese el valor de la altura del primer rectángulo en centímetro: "))
   b2= int(input("Ingrese el valor de la base del segundo rectángulo en centímetro"))
   h2= int(input("Ingrese el valor de la altura del segundo rectángulo en centímetro"))
   a1=obtenerArea(b1,h1)
   a2=obtenerArea(b2,h2)
   p1=calculaPerimetro(b1,h1)
   p2=calculaPerimetro(b2,h2)
   mayor=compararAreas(a1,a2)
   print("El rectándulo 1 tiene un área de %0.2fcm y un perímetro de %0.2fcm" %(a1, p1))
   print("El rectándulo 2 tiene un área de %0.2fcm y un perímetro de %0.2fcm " %(a2,p2))
   print (mayor)
main()