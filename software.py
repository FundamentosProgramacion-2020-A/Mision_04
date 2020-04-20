#Roberto Sobrado
#Calcular costo de paquetes de software

def calcularDescuento(paquetes):
    descuento = 0
    if paquetes >= 1 and paquetes <= 9:
        descuento = ("0%")
        return descuento
    elif paquetes >= 10 and paquetes <= 19:
        descuento = ("13%")
        return descuento
    elif paquetes >= 20 and paquetes <= 49:
        descuento = ("20%")
        return descuento
    elif paquetes >= 50 and paquetes <= 99:
        descuento = ("32%")
        return descuento
    else:
        descuento = ("50%")
        return descuento
def calcularPrecio(paquetes, descuento):
    precio = paquetes*2300*(1+1/descuento)
    return precio
def main():
    paquetes = int(input("¿Cuántos paquetes decesa adquirir?"))
    
    if paquetes > 0:
        descuento = calcularDescuento(paquetes)
        print ("Tu descuento es de: ", (descuento))
    else:
        print ("error")
        
    if paquetes > 0:
        paquetes = int(input("¿Cuántos paquetes decesa adquirir?"))
        descuento = int(input("Cuánto tienes de descuento?"))
        precio = calcularPrecio(paquetes, descuento)
        print ("Tu compra es de $%.2f" % (precio))
    else:
        print ("error")

        #precio = calcularPrecioTotal(paquetes, descuento)
        #print (precio)
        
main()