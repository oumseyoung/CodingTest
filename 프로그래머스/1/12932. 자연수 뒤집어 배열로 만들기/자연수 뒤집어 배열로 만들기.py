def solution(n):
    s = str(n)[::-1]
    result = []
    for i in range(len(s)):
        result.append(int(s[i]))
    return result