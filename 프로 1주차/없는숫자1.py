def solution(numbers):
    a = [1,2,3,4,5,6,7,8,9,0]
    sum = 0
    for num in a:
        if num not in numbers:
            sum += num
    return sum