def solution(n):
    arr = ""
    while n not in (0,1,2):
        arr += str(n % 3)
        n = n//3
    arr += str(n)
    return int(arr,3)