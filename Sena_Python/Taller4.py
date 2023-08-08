from datetime import date

hoy = date.today() # fecha actual
print ("hoy es el día: ", hoy)

print("EJERCICIO DE LAS CLASES DE TRIANGULOS")
a=int(input("digite el valor de A: "))
b=int(input("digite el valor de B: "))
c=int(input("digite el valor de C: "))

if a == b and b == c:
    print("EL TRIANGULO ES EQUILATERO")
elif a==b or b==c or a==c:
    print("EL TRIANGULO ES ISOCELES")
else:
    print("EL TRIANGULO ES ESCALENO")

animal=input("digite un animal: ")
animal= animal.upper()

if animal == "PERRO":
    print("Este animal es el mejor amigo del hombre")
elif animal == "GATO":
    print("Este animal persigue a los ratones")
elif animal == "OSO":
    print("Este animal vive en el polo norte: ", animal)
else:
    print("No es PERRO, no es GATO, ni es OSO... es: ", animal)

print()
print ("FIN")
