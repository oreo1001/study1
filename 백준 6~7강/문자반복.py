T = int(input(''))
for j in range(T):
    r,S= input().split()
    R = int(r)

    for i in S:
        print(i*R,end='')
    print()