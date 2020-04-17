# Autor: Miguel Castillo Ordaz

# Programa que lee número de paquetes vendidos y calcula la cantidad descontada.

# Imprimir pago total y descuento.

def descuentoPorcentaje (paquete):

    if paquete <= (9):
        
        descuento = (0)
        return descuento
    else:

        if  paquete >= (10):

            descuento = (13)
            return descuento
        else:

            if paquete >= (20):

                descuento = (20)
                return decuento
            else:

                if paquete >= (50):

                    descuento = (32)
                    return decuento
                else:

                    if paquete >= (100):

                        descuento = (50)
                        return descuento

def descuentoTotal(paquete, descuento):

    pagoParcial = (paquete*2300)*(descuento/100)
    return pagoParcial


def main():
    paquete = int(input("¿Cuántos paquetes desearía? "))

    if (paquete <= 0):

        print("ERROR: Lo sentimos, la cantidad de paquetes no es válida.")

    else:

        descuento = descuentoPorcentaje (paquete)
        descuentoPorPaquete = descuentoTotal (paquete, descuento)
        
        pagoParcial = (2300*paquete)
        pagoTotal = pagoParcial - descuentoPorPaquete
        print ("Con descuento de: $%.02f" % (pagoParcial))
        print ("Su cantidad a pagar sería de: $%.02f" % (pagoTotal))


main()