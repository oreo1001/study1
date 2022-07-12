def solution(board, moves):
    pick = []
    cnt = 0
    for i in moves:
        for j in range(len(board)):
            doll = board[j][i-1]
            if doll == 0:
                continue
            else:
                pick.append(doll)
                board[j][i-1]= 0
                break
        if len(pick)>1:
            if pick[-1]==pick[-2]:
                cnt +=2
                pick.pop(-1)
                pick.pop(-1)
    return cnt