def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in completion:
        participant.remove(i)
    return participant[0]