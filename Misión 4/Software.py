# Autor: Patricio León
# Escribe un programa que lee el número de paquetes vendidos, calcula la cantidad descontada
# e imprime dicho desceunto y el total a pagar


# Formula para decidir el porcentaje a descontar
def descuentoPorcentaje (paquetes):
    if paquetes <= 9:
        porcentaje = 0
        return porcentaje
    else:
        if  paquetes >= 10:
            porcentaje = 13
            return porcentaje
        else:
            if paquetes >= 20:
                porcentaje = 20
                return porcentaje
            else:
                if paquetes >= 50:
                    porcentaje = 32
                    return porcentaje
                else:
                    if paquetes >= 100:
                        porcentaje = 50
                        return porcentaje
    
    
# Formula para caclcular la cantidad a descontar
def descuentoFinal(paquetes, porcentaje):
    pago = (paquetes * 2300) * (porcentaje/100)
    return pago
                
   
# Programa Inicial   
def main():
    paquetes = int(input("Teclea el número de paquetes ordenados: "))
    
    
    if (paquetes <= 0):
        print("Cantidad de paquetes no valida")
    else:
        porcentaje = descuentoPorcentaje (paquetes)
        descuentoCantidad = descuentoFinal (paquetes, porcentaje)
        pago = 2300*paquetes
        pagoFinal = pago - descuentoCantidad

        print ("Cantidad descontada: $ ",(pago))
        print ("Pago total: $ ",(pagoFinal))
  
  
# Llama a la función principal para resolver el problema  
main()
