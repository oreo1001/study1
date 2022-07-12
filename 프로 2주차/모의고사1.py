def solution(answers):
    stud1 = [1,2,3,4,5]
    stud2 = [2,1,2,3,2,4,2,5]
    stud3 = [3,3,1,1,2,2,4,4,5,5]
    answer = [0,0,0]
    result= []
    for i in range(len(answers)):
        if answers[i] == stud1[i%5]:
            answer[0] += 1
        if answers[i] == stud2[i%8]:
            answer[1] += 1
        if answers[i] == stud3[i%10]:
            answer[2] += 1

    m = max(answer)
    for i in range(len(answer)):
        if answer[i] == m:
            result.append(i+1)

    return result


    #enumerate나 cycle함수를 이용해 할 수도 있다.