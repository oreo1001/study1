N = int(input())
cnt = 0

for i in range(N):
    word = input()
    result = 1
    for i in range(0,len(word)):
        a=word[i]
        if(i+1<len(word)):
            if(word[i]!=word[i+1]):
                for j in range(i+1,len(word)):
                    if(word[j]==a):
                        result = 0
    if result==1 :
        cnt += 1
print(cnt)