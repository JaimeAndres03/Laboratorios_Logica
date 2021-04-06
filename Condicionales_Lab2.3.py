#EJERCICIO 1 - NUMERO MULTIPLO DE 5 Y DE 3
print("<<EJERCICIO 1>> -- NUMERO_MULTIPLO_DE_5_Y_3")
num_u = int(input("Ingrese un numero: "))
if num_u % 5 == 0 and num_u % 3 == 0:
    print("El numero cumple la condición")
else:
    print("El numero no cumple la condición")
#EJERCICIO 1.1 <EXTRA..MAS ESPECIFICO> - DETERMINAR SI EL NUMERO ES MULTIPLO DE 5 Y 3
print("<<EJERCICIO 2>> -- NUMERO_MULTIPLO_DE_5_Y_3")
num_u = int(input("Ingrese un numero: "))
if num_u % 5 == 0 and num_u % 3 == 0:
    print("El numero ingresado es multiplo de 5 Y 3")
elif num_u % 5 == 0:
    print("El numero es multiplo de 5")
elif num_u % 3 == 0:
    print("El numero es multiplo de 3")
else:
    print("El numero ingresado no es multiplo de 5 y de 3")     
#EJERCICIO 2 - CALCULO DEL PROMEDIO DE LAS NOTAS E IMPRIMIR UN MENSAJE
print("<<EJERCICIO 2 -- PROMEDIO_NOTAS_Y_MENSAJE>>")
nota_1 = float(input("Ingrese tu primera nota: "))
nota_2 = float(input("Ingrese tu segunda nota: "))
nota_3 = float(input("Ingrese tu tercera nota: "))
promedio = (nota_1 + nota_2 + nota_3)/3
if promedio >= 7:
    print("Promocionando")
elif promedio >= 4 and promedio < 7:
    print("Regular")
else:
    print("Reprobado")
#EJERCICIO 3 -- PROMEDIO DE NOTAS E IMPRIMIR UN MENSAJE UTILIZANDO 3 CONDICIONALES
print("<<EJERCICIO 3>> -- PROMEDIO_NOTAS_Y_MENSAJE_3_CONDICIONALES")
nota_1 = float(input("Ingrese tu primera nota: "))
nota_2 = float(input("Ingrese tu segunda nota: "))
nota_3 = float(input("Ingrese tu tercera nota: "))
promedio = (nota_1 + nota_2 + nota_3)/3
if promedio >= 7:
    print("Promocionado")
if promedio >= 4 and promedio < 7:
    print("Regular")
if promedio < 4:
    print("No habilitado")
#EJERCICIO 4 -- EJEMPLO DE LISTAS
print("<<EJERCICIO 4>> -- SALUDO_CON_LISTA")
nombres = ["Jaime", "Juan", "Sonia", "Jaime A", "Elvira"]
for n in nombres:
    print("Hola " + n)