print("*EJERCICIO 10* - Primeros_10_numeros_serie_fibonacci")
lim = 10
num_init = 1
num_fib = 0
init = 0
check = "✓"
while init <= lim:
    print("N° {0} {1} ".format(num_fib, check))
    num_init += num_fib
    num_fib = num_init - num_fib
    init += 1