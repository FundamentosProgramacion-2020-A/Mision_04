# Mariana Mejía Béjar
# Calcula el descuento y cantidad a pagar de una venta de software


# Calcula cuánta cantidad de dinero va a ser descontada
def calcularCantidadDescontada(paquetes, descuento):
    cantidadD = 2300 * paquetes *(descuento/100)
    return cantidadD


# Calcula cuánto va a ser el descuento dependiendo del número de paquetes
def calcularDescuento(paquetes):
    if paquetes < 10:
        return 0
    else:
        if paquetes < 20:
            return 13
        else:
            if paquetes < 50:
                return 20
            else:
                if paquetes < 100:
                    return 32
                else:
                    if paquetes >= 100:
                        return 50


# Función principal, se les pregunta al usuario el número de paquetes comprados
# e imprime el subtotal, descuento, cantidad descontado y el total a pagar
def main():
    paquetes = int(input("Escribe el número de paquetes comprados: "))

    if (paquetes <= 0):
        print("ERROR: Ingresa un número válido de paquetes")
    else:
        descuento = calcularDescuento(paquetes)
        cantidadDescontada = calcularCantidadDescontada(paquetes, descuento)
        subtotal=2300*paquetes
        total=subtotal-cantidadDescontada

        print("SUBTOTAL:                  $%d" % subtotal)
        print("DESCUENTO:                 %d%%" % descuento)
        print("CANTIDAD DESCONTADA:       $%d" % cantidadDescontada)
        print("TOTAL A PAGAR:             $%d" %total)


main()
