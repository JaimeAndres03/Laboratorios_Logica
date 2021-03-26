#EJERCICIO 1.2
print("<<< EJERCICIO 1.2 - Numeros_y_cubo_de_los_numeros_del_0_al_20 >>>")
for i in range(21):
    print("Numero {0} y el cubo del numero {1}".format(i, i**3))
#EJERCICIO 1.3
print("<<< EJERCICIO 1.3 - Feliz_año >>>")
for i in range(10, 0, -1):
    print(i)
print("¡Feliz año nuevo!")
#EJERCICIO 1.4
print("<<< EJERCICIO 1.4 - imprimir_hola_de_acuerdo_a_los_numeros_de_la_lista >>>")
for i in [1, 2, 3, 4]:
    print("Hola")
#EJERCICIO 1.5
print("<<< EJERCICIO 1.5 - Numeros_y_cubo_de_los_numeros_del_0_al_20 >>>")
for i in range(5):
    print("Ahora i vale ",i, " y su cuadrado ", i**2)
#Ejercicio 1.6
print("<<< EJERCICIO 1.6 - Imprimir_cada_elemento_de_la_lista >>>")
for i in ['JLo', 'Benito', 'Rosalia', 2021]:
  print("Hola. Ahora i vale", i)
#EJERCICIO 1.7
print("<<< EJERCICIO 1.7 - Numeros_0_al_7 >>>")
for n in range(8):
    print("N°", n)
#EJERCICIO 1.8
print("<<< EJERCICIO 1.8 - Numeros_1_al_12>>>")
for n in range(1, 13):
    print("N° ", n)
#EJERCICIO 1.9
print("<<< EJERCICIO 1.9 - Contador_de_numeros_que_terminan_en_3 >>>")
c = 0
for i in range(1000):
    ultimo_digito = (i**3) % 10
    if ultimo_digito == 7:
        c = c + 1
print(c)
#EJERCICIO 2.01_BLOQUE_ANIDADO
print("<<< EJERCICIO 2.01 - BLoque_anidado>>>")
for i in range(3):
  for j in range(2):
    print("i vale", i, "y j vale", j)
#EJERCICIO 2.02_BLOQUE_ANIDADO
print("<<< EJERCICIO 2.02 - BLoque_anidado>>>")
for i in range(4):
  for j in range(i):
    print("i vale", i, "y j vale", j)
#EJERCICIO 2.1 BLOQUE_ANIDADO
print("<<< EJERCICIO 2.1 - BLoque_anidado>>>")
for x in [1, 3, 5]:
    for a in [0, 2]:
        print("x vale {0} y a vale {1}".format(x, a))
#EJERCICIO 2.11
print("<<< EJERCICIO 2.11 - BLoque_anidado>>>")
for a in [2, 4, 8]:
    for b in range(a):
        print("a vale {0} y b vale {1}".format(a, b))