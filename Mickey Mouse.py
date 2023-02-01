# MICKEY MOUSE
# ROSSINA LUNA
nombre = input("Nombre del Jugador: ")
x = float(input("Ingrese la coordenada x: "))
y = float(input("ingrese la coordenada y: "))
if (x - 1.5) ** 2 + (y - 1.5) ** 2 <= 1.26 or (x + 1.5) ** 2 + (y - 1.5) ** 2 <= 1.26:
    print("Mejor suerte para la proxima", nombre)
elif x ** 2 + y ** 2 <= 0.01:
    print("Ganastes!!", nombre)
elif  x ** 2 + y ** 2 > 0.01 and 0.01 < x ** 2 + y ** 2 <= 1:
    print("Casi")
else:
    print("Que horrible punteria", nombre)
    