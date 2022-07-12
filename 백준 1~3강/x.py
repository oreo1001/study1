c, d = input("").split()
H = int(c)
M = int(d)

if(M>=45):
    print(H,M-45)
elif(M<0 or M>60):
    print("Wrong value!")
else:
    if(H==0):
        print(23,60-45+M)
    elif(H<0 or H>=24):
        print("Wrong value!")
    else:
        print(H-1,60-45+M)










