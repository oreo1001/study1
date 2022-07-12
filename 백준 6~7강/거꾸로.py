a,b = input().split()
ar =''
br =''
for i in range(len(list(a))-1,-1,-1):
    ar += list(a)[i]

for i in range(len(list(b))-1,-1,-1):
    br += list(b)[i]
if(int(ar)>int(br)):
    print(ar)
else:
    print(br)