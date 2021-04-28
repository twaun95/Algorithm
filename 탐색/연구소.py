#https://www.acmicpc.net/problem/14502
n,m = map(int, input().split())

data=[]
for i in range(n):
    data.append(list(map(int, input().split())))
temp = [[0]*m for i in range(n)]#임시 data저장

#동서남북
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def num_zero():
    zero = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                zero += 1
    return zero

#바이러스 퍼트리기

def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx,ny)

count = 0
def dfs(fense):
    global count
    if fense == 3:#울타리3개 설치 됬으면 data를 temp로 옮김
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        
        for i in range(n):#바이러스 전파
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        count = max(count, num_zero())
        return
        
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j]=1
                fense += 1
                dfs(fense)
                data[i][j] = 0
                fense -= 1

dfs(0)
print(count)


            