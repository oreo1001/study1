num = int(input())    
i=1
while num > (i*(i+1)/2):
    i+=1
a = num-i*(i-1)//2
b = i-a+1
if(i%2 ==0):
    print(str(a)+"/"+str(b))
else :
    print(str(b)+"/"+str(a))