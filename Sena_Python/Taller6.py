from datetime import date

hoy = date.today() # fecha actual
print("Hoy es el día:", hoy)
print()
print("TALLER: CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1 = int(input("Digite un número: "))

print("***Ciclo controlado por contador")
i = 1
while i <= num1:
    print(i)
    i += 1
print("Fin del ciclo")

print()
print("***Ciclo controlado por evento")
numero2 = 0
while numero2 != 10:
    numero2 = int(input("Digite un número del 1 al 10: "))
    print("Acertaste en el intento No.", numero2)
print("Fin del ciclo")

print()
print("***Ciclo abortado con la sentencia break")
amistad = input("Digite el nombre de una amistad: ")
amistad = amistad.upper()
for character in amistad:
    print(character)
    if character == "A":
        break
print("Fin del ciclo")
print()
print("FIN")
