'''22. Elaborar un programa que dado un grupo de N valores X e Y (abscisa y
ordenada), correspondiente a las coordenadas de un punto en el plano
determine en cual cuadrante se encuentra el punto, en caso de no
encontrarse en un cuadrante determine si se encuentra en el eje X o Y.'''

n = int(input('Diga el numero de puntos a evaluar:'))
for i in range (n):
    x = float(input('Coordena de la abscisa(x): '))
    y = float(input('Coordenada de la ordenada(y): '))
    if x > 0 and y > 0:
        ubicacion = 'Primer cuadrante'
    elif x < 0 and y > 0:
        ubicacion = 'Segundo cuadrante'
    elif x < 0 and y < 0:
        ubicacion = 'Tercer cuadrante'
    elif x > 0 and y < 0:
        ubicacion = 'Cuarto cuadrante'
    elif y == 0 and x != 0:
        ubicacion = 'Sobre el eje de las abcisas'
    elif x == 0 and y != 0:
        ubicacion = 'Sobre el eje de las ordenadas'
    else:
        ubicacion = 'En el origen'
    print('El punto se encuentra ubicado en:', ubicacion)