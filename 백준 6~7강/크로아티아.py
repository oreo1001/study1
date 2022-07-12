cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()
cnt = 0
for c in cro:
    if(c in word):
        cnt += 1
        wo = word.split(c)
        word = ''
        for a in wo:
            word += a
cnt += len(word)
print(cnt)
    
     