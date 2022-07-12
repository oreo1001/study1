def solution(lottos, win_nums):
    answer = []
    cnt = 0
    cnt2 = 0
    max = 0
    for i in range(len(lottos)):
        if lottos[i] == 0 :
            cnt2 +=1
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1
    max = 7- cnt-cnt2 if cnt+cnt2>=1 else 6
    cnt = 7-cnt if cnt>=1 else 6
    answer.append(max)
    answer.append(cnt)
    return answer

lottos = list(map(int,input().split()))
win_nums = list(map(int,input().split()))

print(solution(lottos,win_nums))