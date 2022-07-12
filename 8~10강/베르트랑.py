import math 
def isPrime(num):
    if num == 1: return False 

    n = int(math.sqrt(num)) 
    for k in range(2, n+1): 
        if num % k == 0: return False
    return True 

while 1:
    n = int(input())
    if n==0 :
        break
    else:
        cnt = 0
        for i in range(n,2*n+1):
            if(isPrime(i)):
                cnt+=1
        print(cnt)