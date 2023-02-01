'''31. Los empleados de una fábrica trabajan en dos turnos: diurnos y nocturnos. 
Dado un conjunto de registros que contienen el nombre del trabajador, día de 
la semana (0=domingo, 1=lunes, 2=martes, etc.), número de horas diurnas y 
número de horas nocturnas trabajadas de un grupo de trabajadores. 
Desarrolle un programa que lea la información indicada y determine para 
cada trabajador el salario diario de acuerdo a lo siguiente:
 La tarifa de las horas diurnas es de Bs. 1.000
 La tarifa de horas nocturnas es de Bs. 1.500
 En caso de ser Domingo la tarifa se incrementará en Bs. 500 el turno diurno 
y Bs. 1.000 el turno nocturno'''
domingo = 0
sabado = 0
viernes = 0
jueves = 0
miercoles = 0
martes = 0
lunes = 0
z = 's'
r = 's'
while z.lower() == 's':
	nombre = input('nombre: ')
	while r.lower() == 's':
		dia = int(input('dia trabajado \n(1) Lunes \n(2) Martes \n(3) Miercoles \n(4) Jueves \n(5) Viernes \n(6) Sabado \n(7) Domingo \n '))
		hdiurnas = int(input('Horas diurnas: '))
		hnocturnas = int(input('Horas nocturnas: '))
		salario = (hdiurnas * 1000) + (hnocturnas * 1500)
		if dia == 1:
			lunes = salario
		elif dia == 2:
			martes = salario
		elif dia == 3:
			miercoles = salario
		elif dia == 4:
			jueves = salario
		elif dia == 5: 
			viernes = salario
		elif dia == 6:
			sabado = salario
		elif dia == 7:
			domingo = (hdiurnas * 1500) + (hnocturnas *2500)
		r = input('Agregar dia? (S/N) \n ')
	semana = lunes + martes + miercoles + jueves + 	viernes + sabado + domingo
	print('Nombre del trabajador:', nombre.title())
	print(f'Salario diario es: \nLunes {lunes:6.2f} \nMartes {martes:6.2f} \nMiercoles {miercoles:6.2f} \nJueves {jueves:6.2f} \nViernes {viernes:6.2f} \nSabado {sabado:6.2f} \nDomingo {domingo:6.2f}')
	print('En la semana cobrara:', round(semana, 2) )
	z = input('añadir nuevo trabajador? (s/n)')
print('No hay mas trabajadores')