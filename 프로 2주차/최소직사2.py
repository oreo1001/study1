def solution(sizes):
    sizes = [sorted(s) for s in sizes]
    return max([x[0] for x in sizes]) * max([x[1] for x in sizes])