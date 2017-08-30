palavra = input("Digite uma palavra: ")

tam = len(palavra)
aux = []
i =0 

for i in range(tam-1) :
	if i == 0:
		#print(pal[i])
		aux.append(palavra[i])
	else:
		aux.append(aux[i-1] + palavra[i] )
	
print("numero de prefixos =  %d" %(len(aux)))	
for k in range(len(aux)):
	print("%d° prefixo = %s" %( k+1 , aux[k]) )
