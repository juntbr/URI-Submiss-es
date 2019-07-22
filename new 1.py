n = int(input())

def verifica(n):
    lista = input().split()
    padrao = 0
    diferenca = 0
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    for i in range(n-1):
        padrao += lista[i]
    for i in range(n):
        diferenca += n-i
    return(diferenca - padrao)

print(verifica(n))
                
           
    
