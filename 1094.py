n = int(input())
totalCobaias, coelho, rato, sapo = 0, 0, 0, 0
for _ in range(0,n):
	q,t = input().split()
	totalCobaias += int(q)
	if t == 'C':
		coelho += int(q)
	elif(t == 'S'):
		sapo += int(q)
	elif(t == 'R'):
		rato += int(q)
percCoelho = (coelho*100)/float(totalCobaias)
percRato = (rato*100)/float(totalCobaias)
percSapo = (sapo*100)/float(totalCobaias)
print("Total: %d cobaias"%totalCobaias)
print("Total de coelhos: %d"%coelho)
print("Total de ratos: %d"%rato)
print("Total de sapos: %d"%sapo)
print("Percentual de coelhos: %.2f %%"%percCoelho)
print("Percentual de ratos: %.2f %%"%percRato)
print("Percentual de sapos: %.2f %%"%percSapo)
