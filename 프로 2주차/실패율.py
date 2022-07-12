def solution(N, stages):
    counts = [0 for i in range(N)] 
    fail = [0 for i in range(N)] 
    gili = len(stages)
    rank = []
    stages.sort()
    for i in range(1,N+1):
        counts[i-1]=stages.count(i)
        fail[i-1]=counts[i-1]/gili
        gili = gili-stages.count(i)
        if gili == 0:
            break
        
    for i in range(1,N+1):
        a = fail.index(max(fail)) #최대값의 인덱스를 a 
        rank.append(a+1)
        fail[a]=-1
    return rank