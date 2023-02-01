'''La empresa EU Compras Inc. permite a sus clientes realizar compras en el
exterior. Para un cliente se registró la compra de un conjunto de artículos,
donde por cada uno de ellos se tiene:
Código del Artículo, Cantidad comprada, Precio Unitario en dólares y

Tipo de Impuesto

Donde el Tipo de Impuesto indica el porcentaje a pagar por concepto de
impuesto; a saber: 0 – Exento (0%), 1 – No Exento (21%)
El precio del dólar se toma como el valor del cambio oficial (1 dólar = Bs. 4.60)
Elabore un programa que lea la información de un cliente, determine e imprima:
    Para cada Artículo:
1. Monto Total en dólares
2. Monto Total en Bolívares
3. Impuesto a Pagar en Bs. según el tipo de Impuesto.
    Para todos los Artículos:
4. Monto Total que el Cliente debe pagar en Bs.
5. Código del Artículo con mayor precio unitario
6. Porcentaje de Artículos Exentos de impuestos'''

#Inicializacion de variables
con_ext = 0
con_art = 0
pmayor = 1
acum_bs = 0
d = float(input('Precio del dolar: '))
r = 0
while r == 0:
    con_art += 1
    art = int(input('Ingrese el código del articulo: '))
    cant = int(input('Cantidad de articulos: '))
    precio = float(input('Precio unitario del articulo: '))
    tipo = int(input('Tipo de impuesto \nExento(0) \nNo exento(1) \n '))
    if precio > pmayor: #Respuesta 5
        pmayor = precio
        art_mayor = art
    if tipo == 0:
#Respuesta3
        impuesto = 0
#Respuesta 1
        monto_d = precio * cant 
        con_ext += 1
    elif tipo == 1:
        impuesto = (precio * 21) / 100
        monto_d = (precio + impuesto) * cant
 #Respuesta 2
    monto_bs = monto_d * d 
    print('El monto en $ es:' , monto_d)
    print('El monto en Bs es:' , monto_bs)
    if tipo == 0:
        print('Exento, impuesto:' , impuesto)
    else:
        print('No exento, impuesto:' , impuesto)
    
#Respuesta 4
    acum_bs += monto_bs
    pregunta = int(input('Agregar articulo \nSI:1 \nNO:2 \n '))
    if pregunta == 2:
        r = 1
print('Monto total Bs:' , round(acum_bs , 2))
print('Articulo con mayor precio unitario:' , art_mayor)
porc = con_ext * 100 / con_art #Respuesta 6
print('El porcentaje de articulos exento es:', round(porc , 2))
    