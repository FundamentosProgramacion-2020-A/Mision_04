#Autor: Samara Andrea Vega
#Leer el número de paquetes vendidos y mostarar el descuento realizado junto con el total a pagar

def calcularPorcentaje(paquete):
    if paquete <=9:
        return "No hay descuento"
    else:
        if paquete <=19:
            return "Descuento de 13%"
        else:
            if paquete <=49:
                return"Descuento de 20%"
            else:
                if paquete <=99:
                    return "Descuento de 32%"
                else:
                    if paquete >=100:
                        return "Descuento de 50%"


def calcularDescuento(paquete):
    precio = 2300*paquete-2300*paquete
    descuentoUno= (2300*.13)*paquete
    descuentoDos= (2300*.20)*paquete
    descuentoTres= (2300*.32)*paquete
    descuentoCuatro= (2300*.50)*paquete
    if paquete <=9:
        return precio
    else:
        if paquete <=19:
            return descuentoUno
        else:
            if paquete <=49:
                return descuentoDos
            else:
                if paquete <=99:
                    return descuentoTres
                else:
                    if paquete >=100:
                        return descuentoCuatro
                    

def main():
    
    paquetes = int(input("¿Cuántos paquetes gusta comprar?"))
    porcentaje = calcularPorcentaje(paquetes)
    print(porcentaje)
        
    descuento = calcularDescuento(paquetes)
    if paquetes <=0:
        print ("ERROR")
    else:
        print("El total con su descuento incluido, es: $%.2f mxn" % descuento)

main()