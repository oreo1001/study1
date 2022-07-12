def solution(a, b):
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    day = b-1
    for i in range(1,a):
        if i in [1,3,5,7,8,10,12]:
            day += 31
        elif i in [4,6,9,11]:
            day += 30
        else:
            day += 29
    #day는 1월1일까지 일수
    return days[(day+5)%7]  #1월1일이 금요일이므로 5를 더해줌   