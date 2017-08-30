"""
1.9. Faça um programa para validar um endereço de e-mail digitado
pelo usuário. O programa deve indicar se o email fornecido
é válido ou não.
"""

nao_pode = ['!','#','$','%','¨','&','*',',',' ','(',')','-','_','+','=']

email = str(input("Digite seu email: "))
tam_email = len(email)
print("Tamanho email: ", len(email))
partes_email = email.split("@")
tam_email2 = 0

cont_erro = 0
cont_ponto = 0
cont_arroba = 0

erro = False

for i in range(len(email)):
  if email[i] in nao_pode:
    cont_erro+= 1
  if email[i] == '@':
    cont_arroba+= 1
  if i != len(email)-1:
    print(email[i] + " -> " + email[i+1])
    if email[i] == '.' and email[i+1] == '.':
      cont_ponto+= 1

msg_erro = ''

#Validando erros
if cont_erro > 0:
  erro = True
  msg_erro = msg_erro + " Caracter especial"
if cont_arroba > 1:
  msg_erro = msg_erro + " Mais de um @"
  erro = True
if cont_ponto > 0:
  msg_erro = msg_erro + " " + str(cont_ponto) + " pontos seguidos"
  erro = True


if erro:
  print("Nao pode caracteres especiais ou repeticoes excessivas de caracteres como @ e . ")  
  print(msg_erro)
else:  
  for k in range(len(email)-1):
    if (ord(email[k]) > 122 ) or (97 > ord(email[k]) > 64) or (46 > ord(email[k]) > 64 or ord(email[k])<46 ):
      cont = 2
      erro = "Voce inseriu um caractere inválido"
  if partes_email[0] == "" or partes_email[1] == "":
    tam_email2 = 0
  else:
    tam_email2 = len(partes_email)
  if tam_email2 != 2:
    print("Nao e email, pois o caracter @ nao aparece ou aparece mais de uma vez ou nao possui prefixo de email")
  else:
    for i in range(tam_email):
      if email[i] == "@":
        ind = i
        print(i)
    if (email[tam_email-1] == "m" or email[tam_email-2] == "o" or email[tam_email-3] == "c" or email[tam_email-4] == "." or email[tam_email-1] == "r" or email[tam_email-2] == "b" or email[tam_email-3] == "." or email[tam_email-4] == "m" or email[tam_email-5] == "o" or email[tam_email-6] == "c"):
      partes_email = email[ind:tam_email-3]
      if partes_email == "":
        print("Nao email")
      else:
        print("E email")
    else:
      print("Nao e email, pois nao possui .com ou .com.br ao final")
