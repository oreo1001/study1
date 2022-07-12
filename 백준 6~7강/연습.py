word = input().upper()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
zero = [0]*26
alp = list(alphabet)

for i in word:
    a = alphabet.index(i)
    zero[a] += 1
max = 0
for i in range(26): #len(zero)
    if(zero[i]>max):
        max = zero[i]
        ans = alp[i]
for i in range(26):
    if(zero[i]==max):
        ans = "?"
print(ans)