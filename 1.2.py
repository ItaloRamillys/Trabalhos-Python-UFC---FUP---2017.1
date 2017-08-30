"""
1.2. Um palíndromo é uma palavra que se pode ler tanto da esquerda para a direita como da direita para a esquerda. Alguns 
exemplos: arara, esse, ovo, rodador, sopapos. Escreva um programa que leia uma cadeia de 
caractertes (string) e indica (imprime) se a cadeia é ou não um palíndromo.
"""
def verificar(palavra):
  m = len(palavra)-1
  verificador = 0
  if len(palavra)%2 == 1:
    t = (len(palavra)//2)+1
  else:
    t = (len(palavra)//2)
  
  for i in range(t):
    if palavra[i] != palavra[m-i]:
      verificador = verificador + 1
  if verificador > 0:
    return "NAO e"
  else:
    return "E"
palavra = str(input("Digite a palavra: "))

print(verificar(palavra))