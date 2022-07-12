def solution(numbers):
    list1=[]
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            a = int(numbers[i])+int(numbers[j])
            answer.append(a) 
    answer = list(set(answer))
    answer.sort()
    return answer