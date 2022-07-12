def solution(numbers, hand):
    answer = ''
    hl=10
    hr=12
    for a in numbers:
        if (a in [1,4,7]):
            answer += "L"
            hl = a
        elif (a in [3,6,9]):
            answer += "R"
            hr = a
        else:
            a = 11 if a == 0 else a
            dl = abs(a-hl) //3+abs(a-hl) %3
            dr = abs(a-hr) //3+abs(a-hr) %3
            if dl > dr:
                answer += "R"
                hr = a
            elif dl < dr:
                answer += "L"
                hl = a
            else :
                if(hand=="right"):
                    answer +="R"
                    hr = a
                else:
                    answer +="L"
                    hl = a
    return answer