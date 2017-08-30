"""
1.1. Escreva um programa que leia uma cadeia de caracteres (string) e gera uma nova cadeia de caracteres
onde todas as letras minúsculas da cadeia original foram trocadas por maiúsculas e vice-versa. 
Caracteres que não são letras (como dígitos, '.', espaço, etc.) não devem ser trocados.
"""

def isCaracter(c,cont):
    for i in range(25):
        if c == vet_mai[i] or c == vet_min[i]:
            cont = 1
    if cont == 1:
      cont = 0
      return True
    else:
      return False

vet_mai = []
vet_min = []
for i in range(25):
    vet_mai.append(chr(65+i))
for i in range(25):
    vet_min.append(chr(97+i))

nova_frase = []

frase = str(input("Digite a frase: "))

for i in range(len(frase)):
  cont = 0
  if isCaracter(frase[i],cont):
      
      for j in range(25):
          if frase[i] == vet_min[j]:
              nova_frase.append(vet_mai[j])
              break
          elif frase[i] == vet_mai[j]:
              nova_frase.append(vet_min[j])
              break
          else:
              j+=1
  else:
      nova_frase.append(frase[i])
frase_nova = ""
for i in range(len(frase)):
  frase_nova = frase_nova + nova_frase[i]
print(frase_nova)