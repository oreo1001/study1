s = input()

eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
for i in eng:
    if s.find(i)>0:
        s = s.replace(i,str(eng.index(i)))
        print(i)
print(s)