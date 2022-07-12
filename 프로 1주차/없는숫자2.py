numbers = list(map(int,input().split()))
def solution(numbers):
    return 45 - sum(numbers)
#solution = lambda numbers: sum(range(10)) - sum(numbers)
print(solution)