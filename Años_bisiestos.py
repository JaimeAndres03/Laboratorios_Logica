print("*EJERCICICO 8* - Años_bisiestos_comprendidos_en_el_rango_de_los_dos_años_ingresados ")
a_i = int(input("Por favor, ingresa el año inicial que comprendera el rango: "))
a_f = int(input("Por favor, ingresa el año final que comprendera el rango: "))
for x in range(a_i, a_f + 1):
    if x % 10 == 0:
        if x % 4 == 0:
            if x % 100 != 0:
                print("Años bisiesto comprendido dentro del rango de los años ingresados: ", x)