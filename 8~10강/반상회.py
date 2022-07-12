testcase = int(input())
for n in range(testcase):
    a = int(input())
    b = int(input())
    lista = [x for x in range(1,b+1)]
    for i in range(a):
        for j in range(1,b):
            lista[j]+=lista[j-1]
    print(lista[b-1])