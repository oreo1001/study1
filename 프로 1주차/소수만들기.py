import math 
from itertools import combinations

def isPrime(num):
    if num == 1: return False 

    n = int(math.sqrt(num)) 
    for k in range(2, n+1): 
        if num % k == 0: return False 
    return True 

def solution(nums):
    answer = 0
    for i in map(sum,combinations(nums,3)):
        if isPrime(i):
            answer +=1

    return answer