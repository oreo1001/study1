def rm_small(mylist):
    mylist.remove(min(mylist))
    return mylist

def solution(arr):
    print(min(arr))
    arr.remove(min(arr))
    if arr ==[]:
        arr.append(-1)
    return arr