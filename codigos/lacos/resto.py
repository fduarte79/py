# calcule o resto de uma divisão inteira usandO operação de adição e subtração

x = int(input('Digite o valor do dividendo: '))
y = int(input('Digite o valor do divisor: '))
temp = x

while temp >= y:
   temp = temp - y

print('Resto: %d' % (temp))
