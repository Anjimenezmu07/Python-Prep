import datetime

hoy = datetime.date.today()
print("Hoy es:", hoy)

print("TALLER: CICLOS ITERATIVOS CON LA SENTENCIA FOR")

num1 = int(input("Digite el primer número: "))
num2 = int(input("Digite el segundo número (mayor): "))

print("Muestro para el primer número:")
for i in range(num1):
    print(i)

print("Muestro del ciclo!")
for i in range(num1, num2):
    print(i)

print("Ciclo desde el primero hasta el segundo número con incrementos de 2")
for i in range(num1, num2, 2):
    print(i)

empresa = input("Digite el nombre de una empresa: ")
print("En carácter de la empresa", empresa)

print("Fin del ciclo")
