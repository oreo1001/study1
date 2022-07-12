a = []
for i in range(9):
    n = int(input(''))
    a.append(n)

i = a.index(max(a))
print(max(a))
print(i+1)