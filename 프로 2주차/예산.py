def solution(d, budget):
    sum = 0
    count = 0
    for i in sorted(d):
        sum += i
        if sum > budget:
            break
        count += 1
    return count