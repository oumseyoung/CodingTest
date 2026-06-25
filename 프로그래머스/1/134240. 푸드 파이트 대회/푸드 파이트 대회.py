def solution(food):
    one = ''
    total = ''
    food = [x//2 for x in food]
    for i in range(1,len(food)):
        one += str(i)*food[i]
    total = one + '0' + one[::-1]
    return total