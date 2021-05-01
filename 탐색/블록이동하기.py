#https://programmers.co.kr/learn/courses/30/lessons/60063
from collections import deque

test = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def movePos(pos, board):
    #dx = [0,1,0,-1]
    #dy = [1,0,-1,0]
    dir = [[0,1], [1,0], [0,-1], [-1,0]]#북동남서
    newPos = []
    x1, y1 = pos[0] #첫번째 좌표
    x2, y2 = pos[1] #두번째 좌표
    # 방향 유지한 채로 4방향 이동
    for dx, dy in dir:
        if board[x1+dx][y1+dy] == 0 and board[x2+dx][y2+dy] == 0: #두좌표 모두 0이 아니면
            newPos.append({(x1+dx, y1+dy), (x2+dx, y2+dy)})#집합형태로 좌표 등록
    # 가로로 있을 때
    if x1 == x2:
        for dx, dy in dir[1::2]:
            if board[x1+dx][y1+dy] == 0 and board[x2+dx][y2+dy] == 0:
                newPos.append({(x1, y1), (x1+dx, y1)})
                newPos.append({(x2, y2), (x2+dx, y2)})
    # 세로로 있을 때
    else:
        for dx, dy in dir[::2]:
            if board[x1+dx][y1+dy] == 0 and board[x2+dx][y2+dy] == 0:
                newPos.append({(x1, y1), (x1, y1+dy)})
                newPos.append({(x2, y2), (x2, y2+dy)})
    return newPos

def solution(board):
    n = len(board)
    extend_board = [[1]*(n+2) for _ in range(n+2)]#범위 벗어나는 외곽을 1로 확장
    for i in range(n):
        for j in range(n):
            extend_board[i+1][j+1] = board[i][j]
    board = extend_board
    pos = {(1,1), (1,2)} #시작위치좌표 #방문처리를 할 떄 {(1,2),(1,1)}과 같은 중복을 방지하기 위해 집합으로
    q = deque()
    visited = [] #방문
    q.append([pos, 0]) #[좌표,이동거리] 큐
    visited.append(pos)
    while q: #bfs
        pos, dist = q.popleft()  #좌표, 이동거리
        dist += 1
        for newPos in movePos(list(pos), board): #이동가능한 좌표들 리턴
            if (n, n) in newPos: #도착지점이 포함되어 있으면 끝
                print(visited)
                return dist
            if newPos not in visited: #아직 방문안했으면
                q.append([newPos, dist])
                visited.append(newPos)
    
    return 0

print(solution(test))