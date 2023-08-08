from datetime import date

hoy = date.today()
print("Hoy es el día:", hoy)

a = int(input("Digite el valor de A: "))
b = int(input("Digite el valor de B: "))

if a >= b:
    print("A es mayor o igual a B")
else:
    print("A es menor que B")

print()

curso1 = "Requerimientos"
curso2 = "Algoritmos"

if curso1 != "Requerimientos" and curso2 != "Algoritmos":
    print("Usted estudia otro programa diferente a Programación de Software")
else:
    print("Usted estudia Programación de Software")

print()

frase = input("Digite una oración: ")
print("La frase en mayúscula es:", frase.upper())

longitud = len(frase)
print("La longitud de la frase es:", longitud, "caracteres")

if longitud > 10:
    print("La frase contiene más de 10 caracteres")
else:
    print("La frase contiene menos de 11 caracteres")

print()
print("FIN")
