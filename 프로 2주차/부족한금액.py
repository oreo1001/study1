def solution(price, money, count):
    sum_pri = 0
    for i in range(1,count+1):
        sum_pri += i*price
    if sum_pri > money:
        answer = sum_pri-money
    else:
        answer = 0
    return answer