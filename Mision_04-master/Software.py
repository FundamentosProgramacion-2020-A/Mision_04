#Autor: Anayansi Alexia tafoya Soto - A01746781
# Calcular la venta de paquetes con descuento

def calcularDescuento (paq):
    
    if paq<10:
        return 0
    else:
        if paq>=10 and paq<=19:
            return 0.13
        else:
            if paq>=20 and paq<=49:
                return 0.20
            else:
                if paq>=50 and paq<=99:
                    return 0.32
                else:
                    if paq>=100:
                        return 0.30
    return descuento    
      
def totalDescuento (paq, calcularDescuento):
    desc = (2300*paq) * calcularDescuento
    return desc

def totalPago (paq, totalDescuento):
    total = (2300*paq) - totalDescuento
    return total

def main():
    paq = int (input( "Teclea la cantidad de paquetes que deseas comprar: "))
    
    descuento = calcularDescuento (paq)
    print ("Tu descuento es de: ", descuento)
    
    desc = totalDescuento (paq, descuento)
    print ("La cantidad que se desconto es de: $", desc)
    
    pago = totalPago (paq, desc)
    print ("El total a pagar es de: $", pago)
    
#Llamar a función principal  
main()