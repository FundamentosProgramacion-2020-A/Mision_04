# Autor: Fernando Pérez González
# Lee el número de paquetes vendidos
# y despliega la cantidad descontada y el total a pagar

def calcularDescuento(cantidadPaquetes):         #calcula el descuento
    
    if cantidadPaquetes >=1 and cantidadPaquetes <=9:
        descuento = 0
    elif cantidadPaquetes >=10 and cantidadPaquetes <=19:
        descuento = 13
    elif cantidadPaquetes >=20 and cantidadPaquetes <=49:
        descuento = 20
    elif cantidadPaquetes >=50 and cantidadPaquetes <=99:
        descuento = 32
    else:
        descuento = 50
        
    return descuento


def calcularCosto(cantidadPaquetes, descuento):  #calcula el costo de los paquetes
    if descuento > 0:
        costo = cantidadPaquetes*2300*(1-(descuento/100))
    else:
        costo = cantidadPaquetes*2300
    return costo


def main():
    cantidadPaquetes = float(input("Ingrese el número de paquetes que quiere comprar: "))
    descuento = calcularDescuento(cantidadPaquetes)
    
    if cantidadPaquetes <=0:
        print("Error, su número de paquetes no es válido")
    else:
        print("El costo final de su orden sería: ", calcularCosto(cantidadPaquetes, descuento))
    
main()
    