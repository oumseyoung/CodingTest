def solution(n):
    arr = ""
    for i in range(n):
        if i % 2 == 1:
            arr += "박"
        else:
            arr += "수"
    return arr