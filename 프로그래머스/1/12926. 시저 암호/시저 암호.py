def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha() and i.isupper():
            new = chr((ord(i)-ord('A')+n)%26+ord('A'))
            answer += new
        elif i.isalpha() and i.islower():
            new = chr((ord(i)-ord('a')+n)%26+ord('a'))
            answer += new
        else: answer += i
    return answer