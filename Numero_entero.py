print("*EJERCICIO 4* - numero_entero_al_doble_-1")
n = int(input("Por favor, ingresa un numero entero positivo: "))
check = "✓"
for x in range(n, n*2):
    print("EL rango del numero ingresado al doble del mismo menos 1 >>>> {0} {1}".format(x, check))
#Otra forma de hacerlo...
print("EJERCICIO 4")
x = int(input("Por favor, ingresa un numero entero positivo: "))
print(list(range(x, x*2)))