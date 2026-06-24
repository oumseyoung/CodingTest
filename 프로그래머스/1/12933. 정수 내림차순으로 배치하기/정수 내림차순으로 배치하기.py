def solution(n):
    nlist = list(map(str, str(n)))
    nlist.sort(reverse=True)
    return int("".join(nlist))