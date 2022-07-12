word = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in range(len(cro)):
    cnt += word.count(cro[i])
print(len(word)-cnt)