# Mariana Ponce Gonzàlez
# Misiòn 4 Venta de Software

#Cantidad descontada
def totaldeproductos(t):
    if t <=10 and t>0:
        total = (t*2300) * .13
    else:
        if t <=49 and t>0:
            total = (t*2300) * .20
        else:
            if t <= 99 and t>0:
                total = (t*2300) * .32
            else:
                if t >=100 and t>0:
                    total = (t*2300) * .50
                else:
                    total = "Error"

    return total

#Descuento total
def totaldelporducto (q):
    if q <=10 and q >0:
        a = (q*2300)-((q*2300) * .13)
    else:
        if q <=49 and q >0:
            a = (q*2300)-((q*2300) * .20)
        else:
            if q <= 99 and q >0:
                a = (q*2300)-((q*2300) * .32)
            else:
                if q >=100 and q >0:
                    a = (q*2300)-((q*2300) * .50)
                else:
                    a = "Error"

    return a

def main():
    p = int(input("Pon cuantos productos se compraron "))
    t = totaldeproductos (p)
    T = totaldelporducto (p)
    
#Porcentaje de descuento 
    if p <=10 and p>0:
        print("Tiene el 13% de descuento")
    else:
        if p <=49 and p>0:
            print("Tiene el 20% de descuento")
        else:
            if p <=99 and p>0:
                print("Tiene el 32% de descuento")
            else:
                if p >=100 and p>0:
                    print("Tiene el 50% de descuento")
                else:
                    print ("Error")

    print("La cantidad de descuento es:", t)
    print("El total de la compra es:", T)
            
main()
    