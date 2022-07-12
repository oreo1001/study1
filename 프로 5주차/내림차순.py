def solution(n):
    a = list(map(int, sorted(str(int(n)))))
    a.reverse()
    str1 = ''
    for i in a:
        str1 = str1 + str(i)
    return int(str1)

    #return int(''.join(sorted(str(int((n)),reverse=True)))