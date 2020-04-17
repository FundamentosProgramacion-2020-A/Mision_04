# Mariana Ponce Gonzàlez
# Misiòn 4 Rectangulos

#funcion para sacar el perimetro
def pericuadrado(a,b):
    p = (a*2)+(b*2)
    
    return p

#funcion para sacar el area 
def areacuadrado(a,b):
    a = a*b
    
    return a

def main():
    #Dimenciones del rectangulo
    lB = int(input("Dame el base del primer rectangulo "))
    lb = int(input("Dame el altura del primer rectangulo "))
    la = int(input("Dame el base del segundo rectangulo "))
    lA = int(input("Dame el altura del segundo rectangulo "))
    q = pericuadrado(lB,lb)
    w = areacuadrado(lB,lb)
    e = pericuadrado(la,lA)
    r = areacuadrado(la,lA)
    
    print("El perimetro del primer rectangulo es %d " % (q))
    print("El area del primer rectangulo es %d " % (w))
    print("El perimetro del segundo rectangulo es %d " % (e))
    print("El area del segundo rectangulo es %d " % (r))
    
    #Que rectangulo tiene la mayor area
    if w>r:
        print ("El primer rectangulo tiene la mayor area")
    else:
        if w<r:
            print ("El segundo rectangulo tiene la mayor area")
        else:
            print ("Los dos rectangulos tienen la misma area")
    
main()

    