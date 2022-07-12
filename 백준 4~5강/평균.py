n = int(input(''))
a = list(map(int,input().split()))
sum=0
M = max(a)
for i in range(n):
    sum+=a[i]/M*100
print(sum/n)