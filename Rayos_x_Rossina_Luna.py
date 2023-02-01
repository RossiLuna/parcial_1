'''La Unidad de Radiología X-Ray realiza cuatro tipos de estudios radiológicos: Cabeza, Tórax, Columna
y Extremidades. Con el objeto de estandarizar el precio de los estudios, se decide ajustarlos de
acuerdo al valor de la Unidad Tributaria definida por el SENIAT cuyo valor para el año en curso se
establece como una constante equivalente a 127 Bs por cada UT. La siguiente tabla muestra los costos
de cada examen:

-Cabeza 2.75 UT
-Tórax 2.50 UT
-Columna 5.25 UT
-Extremidades 2.25 UT

Al final de una jornada de trabajo de la Unidad, se registra en una lista los datos de los N estudios realizados, donde para cada uno
se tiene:

Cédula, Nombre y Edad del Paciente, y el Tipo de estudio realizado (1=Cabeza, 2=Tórax, 3=Columna, 4=Extremidades)

Elabore un programa, que lea la lista con los datos registrados de los N estudios y determine e imprima:

Para cada Estudio:

    1 - Nombre del Paciente, Monto en Bs. del estudio sin IVA, el monto del IVA (8%) y El Monto Total que canceló el paciente.

Para todos los Estudios:

    2 -Suma total recaudada en Bs., sin tomar en cuenta el IVA, y el monto total en Bs. cobrados por IVA
    3 -Promedio de Monto en Bs. sin IVA de los pacientes que se realizaron Estudios de Cabeza o Columna, y cuya edad sea mayor
    a 40 años.
    4 -Porcentaje de Personas con edad comprendida entre 45 y 52 años'''

#INICIALIZACION DE VARIABLES
ut = 127
acum_siva = 0
acum_iva = 0
acum_monto_estudio = 0
cont_pers_estudio = 0
cont_pers_45 = 0
cont_pacientes = 0
n = int(input('Numero de pacientes: '))

for i in range (n):
    cont_pacientes += 1
    
#REPUESTA 1
    
    nombre = input('Nombre del paciente: ')
    cedula = int(input('Cedula del paciente: '))
    edad = int(input('Edad del paciente: '))
    tipo_estudio = int(input('Tipo de estudio \nCabeza(1) \nToraz(2) \nColumna(3) \nExtremidades(4) \n'))
    if tipo_estudio == 1:
        monto = 2.75 * ut
    elif tipo_estudio == 2:
        monto = 2.50 * ut
    elif tipo_estudio == 3:
        monto = 5.25 * ut
    elif tipo_estudio == 4:
        monto = 2.25 * ut
    else:
        print('Tipo de estudio no valido.')
    iva = (monto * 8) / 100
    monto_total = monto + iva
    print('Nombre del paciente:', nombre)
    print(f'Costo del estudio {monto:6.2f} Bs')
    print(f'IVA {iva:6.2f} Bs' )
    print(f'Costo total: {monto_total:6.2f} Bs')
    
#RESPUETA 2
    
    acum_siva += monto
    acum_iva += iva
    
#RESPUESTA 3
    
    if tipo_estudio == 1 or tipo_estudio == 3 and edad > 40:
        cont_pers_estudio += 1
        acum_monto_estudio += monto
        
#RESPUESTA 4
        
    if 45 <= edad <= 52:
        cont_pers_45 += 1
        
prom = acum_monto_estudio / cont_pers_estudio
porc = cont_pers_45 * 100 / cont_pacientes
print(f'Suma total recaudada: {acum_siva:6.2f} Bs')
print(f'Suma total de cobrado por iva: {acum_iva:6.2f} Bs')
print(f'Promedio de pesonas que realizaron estudios de cabeza o columna mayores de 40: {prom:6.2f}')
print(f'Porcentaje de personas con edad comprendida entre 45 y 52: {porc:6.2f} %')