'''El departamento de computación lo contrata a usted para que desarrolle un programa que de los resultados del primer parcial de
un grupo de alumnos, a la cual se le suministra la siguiente información: Nombre del alumno, Hora y minutos de llegada a la prueba.
Si logra entrar a la prueba:
Hora y minutos de salida y calificación obtenida en la prueba.
Procese la información anterior y determine e imprima por consola:
Para cada alumno:
1. Si pudo entrar o no a la prueba indicándolo con un mensaje, en caso de entrar en cuanto tiempo desarrollo la prueba en
horas y minutos.
2. Si llego temprano a la prueba indíquelo con un mensaje y cuánto tiempo espero para entrar a la misma en minutos.
Para todos los alumnos:
3. Porcentaje de alumnos que llegaron temprano con respecto al total que entraron a la prueba.
4. Nombre del alumno que obtuvo la mayor calificación en la prueba habiendo desarrollado la misma en el menor tiempo,
en caso de haber más de un alumno en las mismas condiciones, reporte el primero y el último.
5. Cuantos estudiantes se procesaron antes de encontrar el primer estudiante que no entro a la prueba.
6. Promedio de las notas de los alumnos que llegaron después de transcurridos 45 minutos de haber comenzado la prueba.
Consideraciones:
*Una hora tiene 60 minutos.
*La prueba comienza a las 8:00 AM (480 minutos de día) y termina a las 10:00 AM (600 minutos de día)
Todo alumno que llegue a la 9:01 AM (541 minutos del día) o después no entra a la prueba.'''

#ROSSINA LUNA
#inicializacion de variables
cont_temprano = 0
cont_entro = 0
comienzo = 480
entrada = 541
mayor_nota = -1
tmenor = float(300)
band = 0
band1 = 1
r = 2
cont_nota = 0
acum_nota = 0
while r == 2:
    nombre = input("Ingrese el nombre del estudiante: ")
    hora = int(input("Ingrese su hora de entrada: "))
    min_entrada = int(input("ingrese los minutos de llegada: "))
    hora_llegada = (hora * 60) + min_entrada
    if hora_llegada <= entrada:
        print("si entro a la prueba")
        cont_entro += 1
        hora1 = int(input("Ingrese hora de salida: "))
        min_salida = int(input("ingrese minuto de salida: "))
        nota = float(input("calificacion del estudiante: "))
        hora_salida = (hora1 * 60) + min_salida
        if hora_llegada < comienzo:
            cont_temprano += 1
            tiempo_esp = comienzo - hora_llegada
            tiempo_prueba =  hora_salida -  comienzo
            print(f"Llego temprano y espero {tiempo_esp:5.2f} minutos para entrar")
        else:
            tiempo_prueba = hora_salida - hora_llegada
        tiempo_hora = tiempo_prueba // 60
        tiempo_min = tiempo_prueba - (tiempo_hora * 60)
        print("tardo" ,tiempo_hora,"hora(s) y ", tiempo_min , "minuto(s)") 
# RESPUESTA 4 (falta el primero)

        if  nota > mayor_nota and tiempo_prueba < tmenor:
            mayor_nota = nota
            tmenor = tiempo_prueba
            nombre_mayor = nombre
#RESPUESTA 5
    elif hora_llegada > entrada:
        if band1 == 1:
            nombre_ne = nombre
            est_ant = cont_entro
            band1 = 2
#RESPUESTA 6
        cont_nota += 1
        acum_nota += nota
                
        print("no entro a la prueba")
    pregunta = int(input("Hay más estudiantes 1:SI 2:NO "))
    if pregunta == 2:
        r = 1
# RESPUESTA 3
porc = (cont_temprano / cont_entro) * 100
prom = acum_nota / cont_nota
print(f"Porcentaje de estudiantes que entraron temprano {porc:6.2f} %")
print("El ultimo en tener la mayor nota en el menor tiempo fue: ",nombre_mayor)
print("se contaron", est_ant , "antes del primero que no ingreso")
print("el promedio de las notas de los estudiantes que entraron despues de 45 minutos iniciada la prueba es:" , prom)

        
            



        

       