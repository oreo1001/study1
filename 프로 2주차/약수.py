def solution(left, right):
    sum = 0 
    for i in range(left,right+1):
        if counts(i)%2 ==0:
            sum+= i
        else:
            sum -= i
    answer = sum
    return answer

def counts(num):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    return count