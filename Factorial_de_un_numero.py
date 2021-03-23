print("Factorial_de_un_numero")
num = int(input("Por favor, ingresa un numero entero positivo: "))
f = 1
if num != 0:
    for i in range(1, num + 1):
        f = f * i
print("El factorial del n°{0} ({1}!) es >>>> {2} ".format(num, num, f))