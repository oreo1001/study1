a= int(input(''))
init = a
cnt = 0
while(1):
    b = a//10+a%10 #자릿수를 더한다.
    sum = a%10*10 + b%10 #새로운 수
    cnt +=1
    if(sum == init):
        break
    else:
        a = sum
print(cnt)