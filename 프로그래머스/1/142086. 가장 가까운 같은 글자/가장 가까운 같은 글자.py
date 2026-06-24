def solution(s):
    arr = []
    answer = []
    for i in range(len(s)):
        if s[i] not in arr:
            answer.append(-1)
            arr.insert(0,s[i])
        else:
            answer.append(arr.index(s[i])+1)
            arr.insert(0,s[i])
    return answer