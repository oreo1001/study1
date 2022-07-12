def solution(lottos, win_nums):
    answer = []
    min=0
    max = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            min +=1
    max = 7- min-max if min+max>=1 else 6
    min = 7-min if min>=1 else 6
    answer.append(max)
    answer.append(min)
    return answer

lottos = list(map(int,input().split()))
win_nums = list(map(int,input().split()))

print(solution(lottos,win_nums))