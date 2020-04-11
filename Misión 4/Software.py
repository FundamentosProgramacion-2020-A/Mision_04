# Autor : Sharone Márquez, A01746940
# Escribir un programa que lea el no. de paquetes vendidos y desplegar la cantidad descontada y total a pagar.

#Función para calcular el porcentaje del descuento
def calcularPaquetes(paquetes):
    if paquetes < 10:
        descuento= 0
        return descuento
    else:
        if paquetes <= 19:
            descuento= .13
            return descuento
        else:
            if paquetes <= 49:
                descuento= .20
                return descuento
            else:
                if paquetes <= 99:
                    descuento= .32
                    return descuento
                else:
                    if paquetes >= 10:
                        descuento= .50
                        return descuento


#Función para calcular la cantidad con el descuento 
def calcularDescuento(paquetes, descuento):
    cantidadDes= ((paquetes*2300) * descuento)
    return cantidadDes
        

#Programa inicial
def main():
    paquetes= int(input("Ingrese el no. de paquetes vendidos: "))
    
    
    #Condiciones
    if paquetes < 0:
        print ("ERROR")
    else:
        descuento = calcularPaquetes(paquetes)
        descuentoFinal = calcularDescuento(paquetes, descuento)
        total= (paquetes * 2300) - descuentoFinal
        
        print ("La cantidad descontada es: $%d" % (descuentoFinal))
        print ("El total a pagar es de: $%d" % (total))
        
main()