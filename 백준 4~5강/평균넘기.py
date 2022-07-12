n = int(input(''))
for i in range(n):
    a = list(map(int,input().split()))
    sum = 0
    cnt = 0
    for j in (a[1:]):  #슬라이싱에대해 기억하기
        sum += j
    avg = sum/a[0]
    for k in (a[1:]):
        if(k>avg):
            cnt += 1
    print("%0.3f%%" %(cnt/a[0]*100))  
