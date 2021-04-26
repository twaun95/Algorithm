from collections import deque
import copy
import sys
input = sys.stdin.readline

n, k = map(int,input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

s, x, y = map(int,input().split())

def check_direction(x,y,direction):#북동남서
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    x += dx[direction]
    y += dy[direction]

    return x,y

clear = deque() #큐 감염안된 곳

def bfs(s):
    time = 0
    copyboard = []
    while time < s:       
        for i in range(n): #(0,x좌표,y좌표) 초기화
            for j in range(n):
                if board[i][j] < 0 or board[i][j] > k:
                    clear.appendleft((k+1,i,j))
                    board[i][j] = k+1
        copyboard = copy.deepcopy(board)#deepcopy사용..
        
        while clear:
            virusnum, nx, ny = clear.pop()#1,0          
            for dir in range(4): #북동남서중 최소 값으로 갱신
                a,b = check_direction(nx,ny,dir) #각각의 좌표
                if a>-1 and a<n and b>-1 and b<n: #board범위안에 있으면  
                    board[nx][ny] = min(copyboard[a][b], board[nx][ny])#감염안된 곳 기준 4방향 중 가장 작은 값으로 갱신

        time += 1
        

bfs(s)
if board[x-1][y-1] == k+1:
    print(0)
else:
    print(board[x-1][y-1])