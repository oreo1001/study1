def solution(s, n):
    alp1 = 'abcdefghijklmnopqrstuvwxyz'
    alp2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = ''
    for i in s:
        if i in alp1:
            a = (alp1.find(i)+n)%26
            answer += s[a-1]
        elif i in alp2:
            b = (alp2.find(i)+n)%26
            answer += s[b-1]
    return answer



def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

def caesar(s, n):
    lower_list = "abcdefghijklmnopqrstuvwxyz"
    upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result = []

    for i in s:
        if i is " ":
            result.append(" ")
        elif i.islower() is True:
            new_ = lower_list.find(i) + n
            result.append(lower_list[new_ % 26])
        else:
            new_ = upper_list.find(i) + n
            result.append(upper_list[new_ % 26])
    return "".join(result)