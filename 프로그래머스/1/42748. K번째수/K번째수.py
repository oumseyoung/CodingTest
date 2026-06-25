def solution(array, commands):
    arr = []
    for i in range(len(commands)):
        arr.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return arr