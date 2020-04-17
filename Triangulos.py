# Mariana Ponce Gonzàlez
# Misiòn 4 triangulos

#tipo de triangulo 
def tipodetriangulo(a,b,c):
    if a==b and b==c:
        tt = "Equilatero"
    else:
        if a == c or b == c or a==b:
            tt = "Isoseles"
        else:
            tt = "Otro"
    return tt

def main():
    aa = int(input("Dame el primer lado del triangulo "))
    bb = int(input("Dame el segundo lado del triangulo "))
    cc = int(input("Dame el tercer lado del triangulo "))
  
# si existe el triangulo 
    if aa+bb>cc:
        t = tipodetriangulo (aa,bb,cc)
        print (t)
    else:
        if aa+bb>cc:
             t = tipodetriangulo (aa,bb,cc)
             print (t)
        else:
            if cc+aa>bb:
                t = tipodetriangulo (aa,bb,cc)
                print (t)
            else:
                print ("Estos no corresponden a un triangulo")

main()    