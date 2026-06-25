def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            new = numbers[i] + numbers[j]
            answer.append(new)
    return sorted(list(set(answer)))