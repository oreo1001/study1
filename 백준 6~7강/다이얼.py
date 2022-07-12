dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()
result = 0 
for i in word:
    for li in dial:
        for x in li:
            if(i==x):
                result = result + dial.index(li) +3
print(result)
