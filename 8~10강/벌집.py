a = int(input())
b = (a-1)/3
n=0
while(1):
    n +=1 
    if(n*(n-1)>=b):
        result = n
        break
print(n)