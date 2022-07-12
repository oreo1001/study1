import re

def solution(new_id):
    answer = ''
    id = new_id.lower()
    for i in temp:
        if i == '-' or i == '_' or i == '.' or i.isdigit() or i.isalpha():
            id += i
    id = id.replace("...",".")
    id = id.replace("..",".")
    if(id.find(".")==0):
        id = id[1:]
    l = len(id)
    if l== 0:
        id += "a"
    if l>=16:
        id = id[0:15]
    if id[-1]==".":
        id=id[0:-1]
    if len(id) <= 2:
        t = id[-1]
        while len(id) != 3:
            id += t
    return id