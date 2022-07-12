N = int(input())
div = 2
while N != 1:
    if N%div != 0:
        div+=1
    else:
        print(div)
        N /= div

        
        