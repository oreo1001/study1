list1 = []
for x in range(10500): #10000을 넘을수있으니 조금 넉넉한공간
    list1.append(x+1)
for num in range(1,10000):
    a = list(str(num))
    sum = 0
    for i in a:
        sum += int(i)
    list1[num+sum-1]=0
for ans in range(10000):
    if(list1[ans]!=0):
        print(list1[ans])