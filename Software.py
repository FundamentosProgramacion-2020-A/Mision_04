#Autor: Elena R.Tovar
#Mision_04, Venta de software
#Leer número de paquetes a comprar, calcular descuento
#Imprimir mensaje de error en caso de número negativo
def calcDesc(num):
    if num>=1 and num<=9:
        return 0
    elif num>=10 and num<=19:
        return 13
    elif num>=20 and num<=49:
        return 20
    elif num>=50 and num<=99:
        return 32
    elif num>=100:
        return 50
    else:
        return "CANTIDAD NO VÁLIDA"

def calcularPrecio(num, desc):
    precio=num*(2300*(1-(desc/100)))
    return precio

def main():
    num=int(input("Ingrese el número de paquetes de software que desea comprar:"))
    desc=calcDesc(num)
    precio=calcularPrecio(num,desc)
    if desc=="CANTIDAD NO VÁLIDA":
        print (desc)
    else:
        print("El total de su compra es de $%0.2fMXN"%(precio))
    
    
main()