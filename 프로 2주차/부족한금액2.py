def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

def solution(price, money, count):
    total = (price * (1+count) * count / 2)
    return total - money if total > money else 0 
    #등차수열