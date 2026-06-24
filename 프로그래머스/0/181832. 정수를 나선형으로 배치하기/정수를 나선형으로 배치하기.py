def solution(n):
    answer = [[0]*n for _ in range(n)]
    di = [[0,1], [1,0], [0,-1], [-1,0]]
    x = y = 0
    d = 0
    for i in range(1, n**2+1):
        answer[x][y] = i
        nx = di[d][0] + x
        ny = di[d][1] + y
        if(nx >= n or ny >= n or answer[nx][ny] != 0):
            if d == 3:
                d = 0
            else: d += 1
        x += di[d][0]
        y += di[d][1]
    return answer