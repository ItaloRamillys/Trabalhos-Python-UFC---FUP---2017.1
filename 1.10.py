"""
1.10. Faça um programa para validar uma senha digitada pelo usuário. 
A senha deve ter pelo menos uma letra maiúscula, pelo
menos uma letra minúscula, pelo menos um dígito, deve ter no mínimo 8 e no máximo 15 caracteres. 
"""
senha = str(input("Digite uma senha: "))

"""
Vetores de letras maiusculas e minuscula
"""

vet_min = []
vet_mai = []
vet_num = []

for i in range(25):
	vet_min.append(chr(97+i))
for i in range(25):
	vet_mai.append(chr(65+i))
for i in range(10):
	vet_num.append(str(i))

erro = False

if len(senha) >= 8 and len(senha) <= 15:
  minu = False
  mai  = False
  num  = False
  for i in range(len(senha)):
    if senha[i] in vet_mai:
      mai = True
    elif senha[i] in vet_min:
      minu = True
    elif senha[i] in vet_num:
      num = True
    else:
      erro = True
      print("Algum caracter digitado e invalido")
  if erro:
    print("Senha invalida")
  else:
    if minu == True and mai == True and num == True:
      print("Senha valida")
    else:
      print("Senha invalida")
else:
  print("Sua senha deve possuir de 8 a 15 caracteres")