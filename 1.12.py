"""
1.12. Implemente um programa que leia um ano, no formato dddd, e imprime o ano por extenso.
"""
array_unidades = ['','um', 'dois','tres','quatro','cinco','seis','sete','oito','nove']
array_dez      = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove']
array_dezenas   = ['','dez', 'vinte', 'trinta','quarenta','cinquenta', 'sessenta', 'setenta', 'oitenta','noventa']
array_centenas = ['','cento','duzentos','trezentos','quatrocentos', 'quinhentos', 'seiscentos','setecentos','oitocentos','novecentos']
array_milhar = ['','mil', 'dois mil ','tres mil ','quatro mil ','cinco mil ','seis mil ','sete mil ','oito mil ','nove mil ']

ano = str(input("Digite o ano: "))

nome = []

if len(ano) == 4:
  for i in range(10):
    if int(ano[3]) == i:
      nome.insert(0,array_unidades[i] + " ")
    if int(ano[2]) == i:
      nome.insert(0,array_dezenas[i] + " e ")
    if int(ano[1]) == i:
      nome.insert(0,array_centenas[i] + " e ")
    if int(ano[0]) == i:
      nome.insert(0,array_milhar[i] + " ")
  print(nome)
else:
  print("Formato de data invalido")
