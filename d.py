def solution(strings, n):
    answer = []
    strings = sorted(strings)
    temp = [] 
    for i in range(len(strings)):
       temp.append(strings[i][n])
    temp = sorted(temp)
    print(temp)
        
    return answer