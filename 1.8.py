import random
def fatorial(n):
  fat = 1
  for i in range(1,n+1):
    fat = fat * i
  return fat

palavra = str(input("Digite uma palavra: "))
n = int(input("Digite um numero: "))

fat = fatorial(n)

palavra_cortada = palavra[0:n]

i = 0
nova_palavra = []
combinacoes = []

nova_palavra = list(palavra_cortada)
  
while i < fat:
  random.shuffle(nova_palavra)
  pal = "".join(nova_palavra)
  if pal in combinacoes:
    random.shuffle(nova_palavra)
  else:
    combinacoes.append(pal)
    i+=1

for i in range(fat):
  print("".join(combinacoes[i]))
  
  
  
los