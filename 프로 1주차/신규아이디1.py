import re

def solution(new_id):
    id = ''
    id = new_id.lower()
    id = re.sub("[^a-zA-Z0-9-_.]","",id)
    while ".." in id:
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