def solution(n, lost, reserve):
    for res in reserve:
            for l in lost:
                if res-1 ==l or res+1 ==l:
                    lost.remove(l)
    answer = n-len(lost)
    return answer