n = int(input())
defaultValues = ['GQaku','ISblv','EOYcmw','FPZdnx','JTeoy','DNXfpz','AKUgq','CMWhr','BLVis','HRjt']
for _ in range(0,n):
	senhaFinal = ""
	senha = input()
	for e in senha:
		if e != " ":
			contador = 0
			for x in defaultValues:
				if e in x:
					senhaFinal += str(contador)
					break
				contador += 1
		if len(senhaFinal) == 12:
			break
	print(senhaFinal)
