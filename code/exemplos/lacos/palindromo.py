cont = 1

while True:
  valor = int(input('Digite um valor inteiro: '))
  print("Inteiro: %d, Contador:%d" % (valor, cont))
  if valor < 0: pass         # cont só recebe acréscimo em valor < 0
  elif valor > 0: continue   # se valor > 0, cont não recebe acréscimo
  else: break                # iteração quebra quando valor = 0
  cont = cont + 1            
