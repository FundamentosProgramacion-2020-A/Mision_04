#Autor: Michelle Ojeda Manjarrez
# Calcular el descuento y el total a pagar


#Definir función calcular paquetes
def calcularPaquetes (paquetes):
    if paquetes < 10:
        descuento = 0
        return descuento
    else:
        if paquetes <= 19:
            descuento = 13
            return descuento
        else:
            if paquetes <= 49:
                descuento = 20
                return descuento
            else:
                if paquetes <= 99:
                    descuento = 32
                    return descuento
                else:
                    if paquetes >= 100:
                        descuento = 50
                        return descuento
                    
                    
#Definir función calcular descuento
def calcularDescuento (paquetes, descuento):
    total  = (paquetes * 2300) * (descuento / 100)
    return total


                    
#Función principal
def main ():
    
    
    paquetes = int (input ("¿Cuántos paquetes se han vendido?: "))
    
    descuento = calcularPaquetes (paquetes)
    
    descuentoFinal = calcularDescuento (paquetes, descuento)
    
    totalFinal = (paquetes * 2300) - descuentoFinal
    
    
    #Condicionante
    
    if paquetes <= 0:
        print ("ERROR")
    else:
        print ("La cantidad descontada es: %.02f" % (descuentoFinal))
        print ("El total a pagar es de: $%.02f " % (totalFinal))
    

    
main ()