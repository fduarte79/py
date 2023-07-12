# calculando a raiz quadrada utilizando o método de Newton

x = p2 = n = int(input('Digite um número inteiro positivo: '))
b = 2

while True:
   p1 = (b + (n / b)) / 2
   b = p1
   if p2 - p1 <= 0.000001:
      break
   p2 = p1

print('A raiz quadrada de %d é %.3f' % (x, p1))
