from math import *

def solution(n):
    three = trid(n)
    answer = int(three[::-1],3)
    return answer

def trid(n):
    i=1
    count =0
    answer =''
    while n >= 3*i:  #3의 몇승까지 커버가능?
        count +=1
        i=i*3
        
    for i in range(count,-1,-1):
        div = n//pow(3,i)
        answer += str(int(div))
        n = n%pow(3,i)
    return answer