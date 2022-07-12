N = int(input())
div = 2
square = int(N ** 0.5)
while div <= square:
    if N%div != 0:
        div+=1
    else:
        print(div)
        N //= div
if N > 1:
    print(N)