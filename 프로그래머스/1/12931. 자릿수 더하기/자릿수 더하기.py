def solution(n):
    input = str(n)
    add = 0
    for i in range(len(input)):
        add += int(input[i])
    return add
