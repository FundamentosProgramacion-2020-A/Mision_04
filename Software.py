#Autor: Brandon Julien Celaya Torres - A01745762
#Descripción: lee unidades de software vendida, calcula el descuento y lo aplica al precio.



def calcularPorcentaje(paquetes):
    if paquetes < 10:
        return 0
    else:
        if paquetes <= 19:
            return 13
        else:
            if paquetes <= 49:
                return 20
            else:
                if paquetes <= 99:
                    return 32
                else:
                    if paquetes >= 100:
                        return 50

def cantidadDescuento(paquetes, descuento):
    subtotal= paquetes*2300
    descuentoNum = (descuento*subtotal)/100
    total = subtotal - descuentoNum
    
    
    
    return total
    

def main():
    
    unidades = int(input("¿Cuántos paquetes quieres comprar?: "))
    if unidades < 0:
        print("Número inválido")
    else:
        porcentajeDescuento = calcularPorcentaje(unidades)
        print ("Tu porcentaje de descuento es: %d%% " % (porcentajeDescuento))
        
        cobro = cantidadDescuento(unidades, porcentajeDescuento)
        print ("Tu total a pagar es: $%d" % (cobro))
         
    
    
    



main()