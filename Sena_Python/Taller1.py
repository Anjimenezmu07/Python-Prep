from datetime import date

hoy = date.today()
print("Hoy es el día:", hoy)

n1 = int(input("Digite el primer número: "))
n2 = int(input("Digite el segundo número: "))

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2

print("La suma es =", suma)
print("La resta es =", resta)
print("La multiplicación es =", producto)
print("La división es =", division)

print("FIN PROGRAMA")