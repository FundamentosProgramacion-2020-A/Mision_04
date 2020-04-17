#Kathia Alejandra Cervantes López
#Este programa lee los lados de un triángulo y te dice que tipo de triángulo es

#función para leer información, tomar parametros para la condicón e imprimir
def main ():
    a = float(input("Teclea el primer lado del triángulo: "))
    b = float(input("Teclea el primer lado del triángulo: "))
    c = float(input("Teclea el primer lado del triángulo: "))
    
    #condición para que sea un triángulo
    if (a + b) > c or (b + c) > a or (a + c) > b:
        print ("El triangulo es correcto")
    else:
        print ("No es un triángulo")
        
    #condición para saber que tipo de triángulo es
    if a == b and b == c:
        print ("Es un triángulo equilátero")
    else:
        if a == b or b == c or a == c:
            print ("Es un triángulo isósceles")
        else:
            print ("Otro")  
    
 
main ()