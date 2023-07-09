cont = 1

while True:
  valor = int(input('Digite um valor inteiro: '))
  print("Inteiro: %d, Contador:%d" % (valor, cont))
  if valor < 0: pass
  elif valor > 0: continue
  else: break                # iteração quebra quando valor = 0
  cont = cont + 1            # cont só recebe acréscimo em valor < 0
