#Paulina Mendoza Iglesias
#Programa que imprime descuentos y total a pagar

def calcularDescuentoSoftware(software):
    
    if software >= 10 and software <= 19:
        return 13
    
    elif software >= 20 and software <= 49:
        return 20
    
    elif software >= 50 and software <= 99:
        return 32
    
    elif software >= 100:
        return 50
    
    elif software >= 1 and software <=9:
        return 0
    
    elif software <=0:
        print ("Error")
    

def calcularCantidad(software, descuento):
    costo = software * 2300
    descuentoCantidad = (descuento * costo) / 100
    total = costo - descuentoCantidad
    
    return total


def main():
    
    paquetes = int(input("Cantidad de paquetes de software: "))
    if paquetes <= 0:
        print("Error")
            
    else:
        porcentaje = calcularDescuentoSoftware (paquetes)
        print ("Tu descuento es del %.2f" % (porcentaje))
        
        cuenta = calcularCantidad (paquetes, porcentaje)
        print ("Total a pagar: $ %.2f " % (cuenta))
    
    
main()