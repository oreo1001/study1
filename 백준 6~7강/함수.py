def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

a = list(map(int,input().split()))
print(solve(a))