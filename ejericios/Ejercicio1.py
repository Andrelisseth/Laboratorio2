#Crea una función la cual realice una tabla de multiplicar de n número en Python la cual
#reciba por paramento el numero con el cual desea realizar la tabla de multiplicar, este
#número será obtenido por teclado por parte del usuario.

N=int(input("que tabla de multiplicar quiere realizar"))
if N >0:
    x=1
    while  x <11:
        print(N,"*",x,"=", N*x)
        x +=1
