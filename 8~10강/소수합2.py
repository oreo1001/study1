M = int(input())
N = int(input())

# 반복문 range만큼 리스트를 False로 가득 채움
check = [False for _ in range(N+1)]

# 에라토스테네스의 체를 사용하여 소수를 구해놓기
for i in range(2, int(N**0.6)):
    # 만약 check[i]가 False면 
    if check[i] == False:
        # 소수에 해당하지 않는 부분은 True로 체크해줌
        # ex) 4, 6, 8 etc....
        for j in range(2 * i, N + 1, i):
            check[j] = True
ans = []

for i in range(M, N + 1):
    #만약 i가 2보다 크거나 같으면(1은 소수가 아니기에)
    if i >= 2:
        # 만약 check[i]가 False라면, 즉 소수라면
        if check[i] == False:
            ans.append(i)

if len(ans) == 0:
    print(-1)
else :
    print(sum(ans))
    print(min(ans))