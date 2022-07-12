cnt = 0

def hansu(x):
    global cnt
    if(x//100 + x%10 ==2*(x//10%10)): #100의자리 + 1의자리 = 2*10의자리
        cnt += 1

a = int(input(''))
for i in range(1,a+1):
    if i < 100:
        cnt += 1
    else :
        hansu(i)
print(cnt)