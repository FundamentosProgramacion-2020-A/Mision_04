# Autor: Daniel Rojas, A01376572
# Calcular el total a pagar y el total de descuento de un paquete cuyo precio baja conforme más cantidad se venda.


def seleccionarPorcentaje(cant):   #Selecciona el porcentaje a partir de la cantidad de paquetes adquiridos
    if 0<cant<10:
        percent = 0
    else:
        if 10<=cant<20:
            percent = 13
        else:
            if 20<=cant<50:
                percent = 20
            else:
                if 50<=cant<100:
                    percent = 32
                else:
                    if cant>=100:
                        percent = 50
                    else:
                        percent = -1
    return percent


def calcularDescuento(cant,percent):  #Calcula el dinero que se va a descontar
    discount = (cant*2300)*(percent/100)
    return discount


def calcularPago (cant,discount):  #Calcula el total a pagar por los paquetes.
    pago = (cant*2300)-discount
    return pago


def main():  #Función principal
    cantidad = int(input("¿Cuántos paquetes serán adquiridos? "))  
    porcentaje = seleccionarPorcentaje(cantidad)
    if porcentaje == -1:
        print("ERROR: La cantidad debe ser un número entero positivo. Vuelva a correr el programa.")
    else:
        descuento = calcularDescuento(cantidad,porcentaje)
        total = calcularPago(cantidad,descuento)
        print("""Al comprar esa cantidad de paquetes, se aplicará un descuento de $%.2f.
Por lo tanto, el total a pagar es de $%.2f""" % (descuento,total))

main()
