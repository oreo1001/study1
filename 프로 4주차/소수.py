import math 
def isPrime(num):
    if num == 1: return False 

    n = int(math.sqrt(num)) 
    for k in range(2, n+1): 
        if num % k == 0: return False 
    return True 

def solution(n):
    cnt = 0
    for i in range(1,n+1):
        if(isPrime(i)):
            cnt += 1
    return cnt