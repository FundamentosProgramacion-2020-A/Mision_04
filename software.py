#Autor: Alondra Miranda A01746742
#Ejercicio 3: Software de la Misión 4

def porcentajeDescuento(uni): #Escoje cuál es el descuento indicado
    if uni<10:
        return 0
    else:
        if uni>=10 and uni<20:
            return 0.13
        else:
            if uni>=20 and uni<=49:
                return 0.20
            else:
                if uni>=50 and uni<=99:
                    return 0.32
                else:
                    if uni>=100:
                        return 0.50
                    
                    
def cantidadDescontada(uni, porcentajeDescuento): #Regresa cuánto se te descuenta
    cd = (2300*uni)*porcentajeDescuento
    return cd


def totalPagar(uni,cantidadDescontada): #Te dice cuánto tienes que pagar en total ya con el descuento
    tp = (2300*uni)-cantidadDescontada
    return tp

def main():
    uni = int(input("¿Cuántos paquetes quieres comprar?: "))
    
    descuento = porcentajeDescuento(uni)
    print("El porcentaje que se te descuenta es: ", descuento, "%")
    
    cd = cantidadDescontada(uni, descuento)
    print("La cantidad descontada de tu orden es: $", cd)
    
    tp = totalPagar(uni, cd)
    print("El Total a pagar es: $", tp)
    
    
main()
    







