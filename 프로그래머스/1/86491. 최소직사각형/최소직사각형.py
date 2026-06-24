def solution(sizes):
    maxw = maxh = 0
    for i in range(len(sizes)):
        w = max(sizes[i])
        h = min(sizes[i])
        if w > maxw:
            maxw = w
        if h > maxh:
            maxh = h
    return maxw*maxh
    