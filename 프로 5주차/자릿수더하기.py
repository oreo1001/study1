def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10) 

def sum_digit(number):
    return sum([int(i) for i in str(number)])
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)))