lista = input().split()
lista2 = input().split()
padrao = 0
for i in range(6):
	lista[i] = int(lista[i])
	lista2[i] = int(lista2[i])			
for i in range(6):	
		for x in range(6):
			if (lista[i] == lista2[x]):
	    			padrao +=1 
			
		
if(padrao < 3):
	print("azar")
if(padrao == 3):
	print("terno")
if(padrao == 4):
	print("quadra")
if(padrao == 5):
	print("quina")
if(padrao == 6):
	print("sena")
