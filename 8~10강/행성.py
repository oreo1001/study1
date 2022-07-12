import math

for t in range(int(input())):
    x, y = map(int, input().split())

    distance = y - x
    answer = 0
    if distance == 1:
        answer = 1
    elif distance == 2:
        answer = 2
    else:
        lower = math.floor(math.sqrt(distance))**2 ## 자신 기준 아래의 제곱수
        upper = math.ceil(math.sqrt(distance))**2 ## 자신 기준 위의 제곱수

        if distance - lower < upper - distance: ## 아래의 제곱수와 더 가깝다면
            answer = math.sqrt(lower)*2
        else:
            answer = math.sqrt(upper)*2 - 1

    print(int(answer))