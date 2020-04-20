#Kathia Alejandra Cervantes López
#Este programa calcula un descuento después de ciertos productos comprados

def descontarPaquetes (paquetesVendidos) :
    
    if paquetesVendidos <10:
        descuento = 0
        return (descuento)
    else:
        if paquetesVendidos >= 10 and paquetesVendidos <= 19 :
            descuento = .13
            return (descuento) 
        else:
            if paquetesVendidos >=20 and paquetesVendidos <=49:
                descuento = .20
                return (descuento)
            else:
                if paquetesVendidos >=50 and paquetesVendidos <=99:
                    descuento = .32
                    return (descuento)
                else:
                    if paquetesVendidos >=100:
                        descuento = .50
                        return (descuento) 


def calcularSubtotal (paquetesVendidos):
    paquetes = (paquetesVendidos*2300)
    return paquetes


def calcularDescuento (paquetesVendidos, descuento):
    paquetesDescuento = ((paquetesVendidos*2300)*descuento)
    return paquetesDescuento


def calcularTotal (paquetesVendidos, descuento) :
    total = (paquetesVendidos*2300 - (paquetesVendidos*2300)*descuento)
    return total

def main ():
    
    paquetesVendidos = float(input("¿Cuántos paquetes vas a comprar? "))
    if paquetesVendidos <=0:
        error = "La cantidad de compra de paquetes es errónea"
        print (error)
    
    else:
        descuento = descontarPaquetes (paquetesVendidos)
        print ("El porcentaje de descuento es de", (descuento))
        
        subtotal = calcularSubtotal (paquetesVendidos)
        print ("El subtotal es de $", (subtotal))
        
        descuentoPaquetes = calcularDescuento (paquetesVendidos, descuento)
        print ("El descuento es de $", (descuentoPaquetes))
        
        totalPagar = calcularTotal (paquetesVendidos, descuento)
        print ("El total a pagar es $", (totalPagar))
    


main ()
