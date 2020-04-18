#José Manuel Rivera Sosapavón
#Software

def calcularPago(unidades):
    if unidades >= 1 and unidades <= 10:
        total = 2300
    elif unidades >= 11 and unidades <= 19:
        total = 2300 *.87
    elif unidades >= 20 and unidades <=49:
        total = 2300 *.80
    elif unidades >= 50 and unidades <=99:
        total = 2300 *.68
    else:
         total = 2300 *.50
    
    return total
    
def calcularDescuento(unidades):
    if unidades >= 1 and unidades <= 10:
        total = 2300
    elif unidades >= 11 and unidades <= 19:
        descuento = 13
    elif unidades >= 20 and unidades <=49:
        descuento = 20
    elif unidades >= 50 and unidades <=99:
        descuento = 32
    else:
         descuento = 50
    
    return descuento

def main():
    u = float(input("Numero de unidades: "))
    discount = calcularDescuento(u)
    print ("Porcentaje de descuento aplicado:%.2f " %(discount))
        
    if u >=0:
        total = calcularPago(u)
        print("Total a pagar: $%.2f" % (total))
        
    else:
        print("ERROR, Inserte una cantidad valida")
        
       
                
        
main()