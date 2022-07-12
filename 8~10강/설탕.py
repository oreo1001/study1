a = int(input())
if a%5 == 0:
    res = a//5
elif a<3 or a==4: res = -1
else :
    nam = a%5
    div = a//5
    if(nam%3 == 0):
        res = a//5 + nam//3
    elif(a%3 ==0):
        res = a//3
    else:
        for i in range(1,div+1):
            if((a-5*i)%3==0):
                res = i+ (a-5*i)//3
                break
            else:
                res = -1
print(res)