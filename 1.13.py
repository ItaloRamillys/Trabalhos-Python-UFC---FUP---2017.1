"""
Implemente um programa que gere aleatoriamente um CAPTCHA de seis caracteres, o qual obrigatoriamente deve conter: letras
maiúsculas, letras minúscula e dígitos. O programa deve exibir o CAPTCHA gerado e solicitar que o usuário digite o valor
exibido. Em seguida, o programa deve ler o texto digitado pelo usuário e verificar se este corresponde ao CAPTCHA gerado.
Observe que, durante esta comparação, não se faz diferença entre letras maiúsculas ou minúsculas. O programa deveimprimir
uma mensagem dizendo se o usuário passou ou não do teste.
"""
from random import *

vet_min = []
vet_mai = []
vet_num = []

vet_captcha = []

#Criando vetores
for i in range(25):
	vet_min.append(chr(97+i))
for i in range(25):
	vet_mai.append(chr(65+i))
for i in range(10):
	vet_num.append(i)

continuar = True

minu = False
mai = False
num = False

verificador = False

while continuar:
  for i in range(6):
        n = randint(0,2)
        if n == 0:
          vet_captcha.append(vet_min[randint(0,24)])
          minu = True
        elif n == 1:
          vet_captcha.append(vet_mai[randint(0,24)])
          mai = True
        else:
          num = True
          vet_captcha.append(vet_num[(randint(0,9))])
  if minu == False or mai == False or num == False:
    print(vet_captcha)
    print("Limpando captcha")
    mai = False
    minu = False
    num = False
    vet_captcha.clear()
    print(vet_captcha)
  else:
    continuar = False
    captcha = ""
    for i in range(6):
      captcha = captcha + str(vet_captcha[i])


print("Digite o seguinte CAPTCHA:")

print(captcha)

resposta = str(input("Digite o captcha por favor:"))

if resposta == captcha:
  print("Acertou")
else:
  print("Errou")
  
  
      
    
      
      
      