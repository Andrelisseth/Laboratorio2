#Pide por teclado el nombre, edad y salario y muestra el salario.
#▪ Si es menor de 16 no tiene edad para trabajar
#▪ Entre 19 y 50 años el salario es un 5 por ciento más
#▪ Entre 51 y 60 años el salario es un 10 por ciento más
#▪ Si es mayor de 60 el salario es un 15 por ciento más

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
descuento=0.0
if(edad<16):    
    print('No tienes edad para trabajar')
    print('Nombre: ',nombre,'\nEdad: ',edad)
elif(edad>=19 and edad<=50):
    salario = float(input('Ingrese sus alario base: '))
    descuento=salario*0.05
    salario=salario+descuento
    print('Nombre: ',nombre,'\nEdad: ',edad,'\nSalario: ',salario)
elif(edad>=51 and edad<=60):
    salario = float(input('Ingrese sus alario base: '))
    descuento=salario*0.10
    salario=salario+descuento
    print('Nombre: ',nombre,'\nEdad: ',edad,'\nSalario: ',salario)
elif(edad>60):
    salario = float(input('Ingrese sus alario base: '))
    descuento=salario*0.15
    salario=salario+descuento
    print('Nombre: ',nombre,'\nEdad: ',edad,'\nSalario: ',salario)