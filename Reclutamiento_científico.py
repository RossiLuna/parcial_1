'''Proyecto 9: Reclutamiento científico
Un científico loco realiza una investigación para poder
determinar el rendimiento de un grupo de estudiantes de la
Facultad de Ingeniería de la Universidad de Carabobo, y así
tener nuevos reclutas para que trabajen en su laboratorio,
para ello realiza una recolección de datos y por cada
estudiante obtiene:

Nombre del estudiante, Escuela a la que pertenece.
Tiempo invertido para resolver el primer parcial (en
minutos). Tiempo invertido para resolver el segundo

parcial (en minutos).

Ante esta situación, este científico, desesperado, lo llama a
usted, que es un brillante estudiante de la materia de Computación I de la Facultad de Ingeniería de la UC para
que desarrolle un programa que determine e imprima:
1. Tiempo promedio en minutos que invirtió cada estudiante para resolver los parciales.
2. Un mensaje que indique, por cada estudiante, si esta reclutado o no.
3. Porcentaje de estudiantes que este científico reclutará.
4. Nombre del estudiante que será el asistente directo de este científico loco.
CONSIDERACIONES
• La escuela se maneja como: “ELECTRICA”, “INDUSTRIAL”, “CIVIL” Y “QUIMICA”.
• Este científico reclutará a todo estudiante que haya invertido en promedio, menos de una hora y media para resolver los
parciales.
• El asistente directo del científico será aquel estudiante, perteneciente a la escuela de eléctrica que haya invertido en promedio,
el menor tiempo para resolver los parciales. En caso de existir más de uno con el mismo tiempo, el científico se quedará con el
primero que logro el cometido.

1 hora equivale a 60 minutos.'''


primero = 'no hay primero'
con = 0
con_rec = 0
r = 1
tmenor = 90
band = 0
while r == 1:
    nombre = input('Nombre del estudiante: ')
    escuela = int(input('Nombre de la escuela \n1 = Electrica  \n2 = Civil \n3 = Industrial \n4 = Quimica \n '))
    parc1 = int(input('Minutos de realiazacion del parcial 1: '))
    parc2 = int(input('Minutos de realizacion del parcial 2: '))
    prom = (parc1 + parc2) / 2
    print('Promedio de realizacion de los examenes: ', prom)
    if prom < 90:
        rec = 'Si'
        con_rec += 1
    else:
        rec = 'No'
    print('Reclutado: ', rec)
    con += 1
    if escuela == 1:
        if prom < tmenor:
            tmenor = prom
            band = 0
        if band == 0:
            primero = nombre
            band = 1
    r = int(input('Desea agregar otro estudiante \n1 = SI \n2 = NO \n '))
porc  = (con_rec / con) * 100
print(f'Porcentaje de estudiantes reclutados {porc:6.0f}')
print('Asistente directo', primero.upper())

            