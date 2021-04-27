from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
n, l, r = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

def bfs(i, j):
    q = deque()
    q.append([i, j])
    sum_all = s[i][j] 
    connect = []
    connect.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                if l <= abs(s[nx][ny] - s[x][y]) <= r:
                    sum_all += s[nx][ny]
                    visit[nx][ny] = 1
                    q.append([nx, ny])
                    connect.append([nx, ny])

    return connect,sum_all


result = 0
while True:
    visit = [[0] * n for i in range(n)]
    move = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0:
                visit[i][j] = 1
                connect, sum_all = bfs(i, j)
                if len(connect) > 1:
                    move = True
                    for x, y in connect:
                        s[x][y] = sum_all // len(connect)
    if move == False:
        break
    result += 1
print(result)