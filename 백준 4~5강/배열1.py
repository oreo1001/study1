a = int(input(''))
b = list(map(int,input().split()))
min = 1000000
max = -1000000
for i in range(a):
    if(b[i]<=min):
        min = b[i]
    elif(b[i]>=max):
        max = b[i]
print(min,max)