pal = input("Insira uma palavra: ")

tam = len(pal) -1
aux = []
i =0 


for i in range(tam , 0 ,-1) :
	if i == tam:
		print(i)
		aux.append(pal[i])
	else:
		aux.append (pal[i] + aux[(tam-1)-i])
		
print("numero de sufixos =  %d" %(len(aux)))	
for k in range(len(aux)):
	print("%dÂ° sufixo = %s" %( k+1 , aux[k]) )

