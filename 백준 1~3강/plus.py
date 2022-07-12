a = int(input(""))

for i in range(1,a+1):
    b,c = input("").split()
    n1 = int(b)
    n2 = int(c)
    print("Case #%d: %d + %d = %d" %(i,n1,n2,n1+n2))