"""
1.3. Escreva um programa que leia uma cadeia de caracteres (string) que 
represente o nome completo de uma pessoa e imprima o
mesmo nome no formato indicado nos exemplos a seguir. Se a String 
recebida for “Maria de Sá Santos” o programa deve
imprimir “Santos, Maria de Sá” . Se a String recebida for 
“Pedro de Souza” o programa deve imprimir “Souza, Pedro de”.
"""
nome = str(input("Digite seu nome: "))
vet_nome = nome.split()
if len(vet_nome)>1:
  primeiro_nome = vet_nome[len(vet_nome)-1]
  resto_nome    = " ".join(vet_nome[0:(len(vet_nome)-1)])
  print(primeiro_nome, ",",resto_nome)
else:
  print("Por favor digite nome e sobrenome")