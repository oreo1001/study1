testcase = int(input())
for i in range(testcase):
    H,W,N = map(int,input().split())
    if(N%H==0):
        front = H
        back = N//H
    else:
        front = N%H
        back = N//H + 1
    print(front*100+back)