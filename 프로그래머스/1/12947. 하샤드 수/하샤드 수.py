def solution(x):
    xlist = list(map(int, str(x)))
    s = sum(xlist)
    if x % s == 0:
        return True
    else: return False