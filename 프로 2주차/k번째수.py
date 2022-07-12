def solution(array, commands):
    answer1 = []
    for i in range(len(commands)):
        a = commands[i]
        answer = array[a[0]-1:a[1]]
        answer.sort()
        answer1.append(answer[a[2]-1])
    return answer1