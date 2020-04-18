#Autor: Valeria Huerta Pedregal
#Calcular la cantidad descontada y el total a pagar de paquetes de software

def calcularDescuento(paquetes):
    if paquetes >= 1 and paquetes <=9:
        descuento = 0
    if paquetes >= 10 and paquetes <= 19:
        descuento = 13
    elif paquetes >= 20 and paquetes <= 49:
        descuento = 20
    elif paquetes >= 50 and paquetes <= 99:
        descuento = 32
    else:
        if paquetes >=100:
            descuento = 50
    
    return descuento

def calcularPago(paquetes,descuento):
    if descuento > 0:
        pago = paquetes*2300*(1-(descuento/100))
    else:
        pago = paquetes*2300
    return pago

def main():
    paquetes = int(input("Ingrese el número de paquetes que desea comprar: "))
    
    if paquetes <= 0:
        print("Error")
    else:
        print("El porcentaje de descuento es",calcularDescuento(paquetes))
        descuento = calcularDescuento(paquetes)
        pago = calcularPago(paquetes, descuento)
        print("El total a pagar es $%.2f" % pago)
    
main()
    
    
        