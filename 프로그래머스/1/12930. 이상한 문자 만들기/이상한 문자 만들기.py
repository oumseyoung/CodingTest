def solution(s):
    answer = ""
    slist = s.split(' ')
    for i in range(len(slist)):
        for j in range(len(slist[i])):
            if j % 2 == 0:
                answer += slist[i][j].upper()
            else: answer += slist[i][j].lower()
        if i != len(slist)-1: answer += " "
    return answer