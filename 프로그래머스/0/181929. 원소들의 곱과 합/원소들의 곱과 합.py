def solution(num_list):
    x=1
    s = sum(num_list)
    for num in num_list:
        x *= num
    if x < s**2:
        return 1
    else:
        return 0