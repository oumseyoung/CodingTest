def solution(strings, n):
    answer = [0]*len(strings)
    nlist = []
    for i in range(len(strings)):
        nlist += strings[i][n]
    nlist.sort()
    strings.sort()
    for i in range(len(strings)):
        index = nlist.index(strings[i][n])
        nlist[index] = 0
        answer[index] = strings[i]
    return answer