def solution(answers):
    stud1 = [1,2,3,4,5]
    stud2 = [2,1,2,3,2,4,2,5]
    stud3 = [3,3,1,1,2,2,4,4,5,5]
    answer = []
    count1= 0
    count2= 0
    count3= 0
    for i in range(len(answers)):
        if answers[i] == stud1[i%5]:
            count1 += 1
        if answers[i] == stud2[i%8]:
            count2 += 1
        if answers[i] == stud3[i%10]:
            count3 += 1
    if count1 > count2:
        if count1 >count3:
            answer.append(1)
        elif count1 < count3:
            answer.append(3)
        else:
            answer.append(1)
            answer.append(3)
    elif count1 < count2:
        if count2 >count3:
            answer.append(2)
        elif count2 < count3:
            answer.append(3)
        else :
            answer.append(2)
            answer.append(3)
    else :
        if count1 == count3:
            answer.append(1)
            answer.append(2)
            answer.append(3)
        else :
            answer.append(1)
            answer.append(2)
    return answer