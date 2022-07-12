n = int(input())
for j in range(n) :
    sum = 0
    score = 0
    quiz = list(input(''))
    for i in quiz :
        if(i == "O") :
            score += 1
        else :
            score = 0
        sum += score
    print(sum)