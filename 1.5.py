"""
1.5. Implemente um programa que leia uma cadeia de caracteres e um caractere. 
O programa deve retirar da cadeia todas as
ocorrências desse caractere. Imprimir a nova cadeia.
"""
palavra = str(input("Digite a palavra: "))
caracter = str(input("Digite o caracter: "))

palavra_nova = ""

if len(caracter) == 1:
  for i in range(len(palavra)):
    if palavra[i] != caracter:
      palavra_nova = palavra_nova + palavra[i]
  print(palavra_nova)
else:
  print("Caracter digitado invalido.")