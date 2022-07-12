def isprime(num):
    for i in range(2,num):
        if num % i ==0:
            return 0
            break
    return 1
M = int(input())
N = int(input())

lista = []
for n in range(M,N):
    if(isprime(n)==1):
        lista.append(n)

if(len(lista)):
    print(sum(lista))
    print(lista[0])  
else:      
    print(-1)