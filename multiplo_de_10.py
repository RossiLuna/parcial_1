#CALCULO DEL MULTIPLO DE 10
a = int(input('Diga un número: '))
n = 10 % a
if (n == 0 and 3000 < a < 4000):
    print('true')
else:
    print('false')
    