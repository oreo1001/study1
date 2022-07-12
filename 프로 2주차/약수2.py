def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:  #약수의 갯수가 홀수면 제곱수이다.
            answer -= i
        else:
            answer += i
    return answer
