print("*EJERCICIO 6* - vocales_dentro_de_una_frase")
frase = input("Por favor, ingresa una frase: ")
for x in "aeiou":
    if x in frase:
        print("Vocal dentro de la frase que ingresaste >>> ", x)