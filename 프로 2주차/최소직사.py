def solution(sizes):
    maxi = []
    mini = []
    for i in range(len(sizes)):
        if sizes[i][0]>=sizes[i][1]:
            maxi.append(sizes[i][0])
            mini.append(sizes[i][1])
        else :
            maxi.append(sizes[i][1])
            mini.append(sizes[i][0])
    answer= max(maxi) * max(mini)
    return answer