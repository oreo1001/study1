alphabet = 'abcdefghijklmnopqrstuvwxyz'
p = [-1]*26
S = input('')
for i in S:
    for j in alphabet:
        if(i==j):
            p[alphabet.index(j)]=S.index(i)
for k in p:
    print("%d " %k,end='')