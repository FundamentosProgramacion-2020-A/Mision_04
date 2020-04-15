# Autor: Paloma Argelia Cueto González
# Programa que recibe la cantitdad de paquetes vendidos y muestra
# el procentaje de descuento y el precio final.

# Función para conocer el porcentaje de descuento
def calcularPorcentaje(cantidad):
    if cantidad <= 9 and cantidad >= 1:
        descuento = 0
        return descuento
    else:
        if cantidad >= 10 and cantidad <= 19:
            descuento = 13
            return descuento
        else:
            if cantidad >= 20 and cantidad <=49:
                descuento = 20
                return descuento
            else:
                if cantidad >= 50 and cantidad <=99:
                    descuento = 32
                    return descuento
                else:
                    cantidad >=100
                    descuento = 50
                    return descuento

# Función para calcular descuento
def calcularDescuento(cantidad, descuento):
    total = (cantidad * 2300) * (descuento/100)
    return total

# Función principal
def main ():
    
    cantidad = int (input ("Ingresa cuántos paquetes compraste: "))
    
    descuento = calcularPorcentaje(cantidad)
    
    descuentoFinal = calcularDescuento(cantidad, descuento)
    
    totalFinal = (cantidad * 2300) - descuentoFinal
    
    # Condición
    
    if cantidad <= 0:
        print ("Error")
    else:
        print ("El descuento hecho fue de: $%.2f" % (descuentoFinal))
        print ("El total a pagar es de: $%.2f" % (totalFinal))
    
main ()    