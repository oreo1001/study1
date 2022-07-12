def solution(s):
    answer = ''
    a = []
    for i in s:
        a.append(i)
    if len(a) % 2 == 0:
        answer = a[(len(a)//2) - 1] + a[(len(a)//2)]
    else:
        answer = a[(len(a)//2)]
    return answer