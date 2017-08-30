"""
1.4. Escreva um programa que leia duas cadeias de caracteres (string) e verifica se uma é 
anagrama de outra. Anagrama é uma palavra formada pela transposição das 
letras de outra, como, por exemplo: 'capa' e 'paca';'roma' e 'mora'.
"""
palavra1 = str(input("Digite a palavra: "))
palavra2 = str(input("Digite a palavra: "))

vetor = list(palavra1)

if len(palavra1) == len(palavra2):
  for i in range(len(palavra1)):
    for j in range(len(palavra2)):
      if palavra2[i] == vetor[j]:
        vetor.remove(palavra2[i])
  
  if len(vetor) == 0:
    print("É anagrama")
  else:
    print("Nao e")
else:
  print("As palavras possuem tamanho diferentes.")