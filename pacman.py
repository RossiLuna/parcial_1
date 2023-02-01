'''
El famoso buscador Google ha querido celebrar el 30 aniversario de Pac Man transformando su logo en un videojuego interactivo que el usuario puede utilizar moviendo las flechas de su teclado.
Este minijuego cuenta con todas las funciones del proyecto original: desde la música y los enemigos,
hasta los 256 niveles desarrollados por la empresa japonesa Namco. La cabecera de la página del buscador se convierte en la tradicional pantalla del videojuego
aunque en esta ocasión es alargada y las paredes forman la palabra "Google".
La reacción de los fanáticos de este juego no se hizo esperar y Google detecto que los mismos
destinaban horas para entretenerse con PacMan. Para continuar la celebración, Google decidió premiar a los mejores jugadores, para ello, registra para cada una de las personas que jugaron:
	
Nombre del jugador, país de residencia, sexo del jugador,
 tiempo que duró jugando, puntaje obtenido

En base a la información anterior, desarrolle una aplicación de consola en VB2008 que determine e imprima:
	
1. Nombre y país del jugador que obtuvo el mejor puntaje.
2. Cantidad total de jugadores que participaron.
3. Porcentaje de jugadores que duraron más de 120 minutos jugando.
4. Puntaje promedio obtenido por los jugadores.
5. Nombre de la primera persona que duro menos de 40 minutos jugando.
6. Puntaje promedio obtenido por los jugadores de sexo femenino.
'''
pmayor = -1
r = 's'
band = 1
conj = 0
con120 = 0
acumpts = 0
acumfem = 0
contfem = 1

while r.lower() == 's':

	nombre = input('nombre; ')
	pais = input('pais; ')
	sex = int(input('genero \nfemenino: 1 \nmasculino: 2 \n'))
	tiempo = float(input('tiempo en minutos de juego: '))
	pts = float(input('puntaje obtenido; '))
#Respuesta 1
	if pts > pmayor:
		pmayor = pts
		nombremejor = nombre
		paismejor = pais
#Respuesta 2
	conj += 1
#Respuesta 3
	if pts > 120:
		con120 += 1
# Respuesta 4
	acumpts += pts
#Respuesta 5
	if tiempo < 40 and band == 1:
		nombremenor = nombre
		band = 0
# Respuesta 6
	if sex == 1:
		acumfem += pts
		contfem += 1
	r = input('añadir jugador, [S/N]: ')
porc = (con120 * 100) / conj
promj = acumpts / conj
promfem = acumfem / contfem
print('el mejor jugador fue',nombremejor,'del pais de;', paismejor)
print('participaron', conj,'jugadores')
print(porc, '% de los jugadores duraron mas de 120 minutos')
print('el puntaje promedio de los jugadores es;', promj)
print('la persona que duro menos tiempo jugando fue;',nombremenor )
print('las mujeres tubieron un puntaje promedio de;', promfem)
		
