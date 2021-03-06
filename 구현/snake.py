#뱀
"""
'Dummy'라는 도스 게임이 있습니다. 이 게임에는 뱀이 나와서 기어 다니는데, 사과를 먹으면 뱀 길이가 늘어납니다. 뱀이 이리저리 기어 다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝납니다.
게임은 N X N 정사각 보드 위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있습니다. 보드의 상화좌우 끝에는 벽이 있습니다. 게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1입니다.
뱀은 처음에 오른쪽을 향합니다.
뱀은 매 초마다 이동을 하는데 다음과 같은 규치을 따릅니다.
  - 먼저 뱀은 몸길이를 늘려 머리를 다음 칸에 위치시킵니다.
  - 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않습니다.
  - 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줍니다. 즉, 몸길이는    변하지 않습니다.
사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하세요.

*입력조건
- 첫째 줄에 보드의 크기 N이 주어집니다. (2<=N<=100) 다음 줄에 사과의 개수 K가 주어집니다.(0<=K<=100)
- 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미합니다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측(1행 1열)에는 사과가 없습니다.
- 다음 줄에는 뱀의 방향 변환 횟수 L이 주어집니다.(1<=L<=100)
- 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자C로 이루어져 있으며, 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')으로 90도 방향을 회전시킨다는 뜻입니다. X는 10000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어집니다.

*출력조건
- 첫째 줄에 게임이 몇 초에 끝나는지 출력합니다.

*입력예시                   *출력예시
6                           9
3
3 4
2 5
5 3
3
3 D
15 L
17 D
"""

#보드크기
n = int(input())
#사과개수
k = int(input())

#보드
data = [[0]*(n+1) for _ in range(n+1)]

#보드에서 사과 위치 설정 (1로)
for _ in range(k):
  a,b = map(int, input().split())
  data[a][b] = 1
print(data)
#방황변환횟수
info = []
l = int(input())
for _ in range(l):
  x,c = input().split()
  info.append((int(x), c))

print(info)

#방향설정 동(0),남(1),서(2),북(3) 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c):
  if c == "L":
    direction = (direction-1)%4
  else:
    direction = (direction+1)%4
  
  return direction  

#처음 방향은 동쪽으로 가면서 시작
direction = 0 

#메인시작

def simulate():
  x,y = 1,1 # 현재 뱀의 머리 위치
  data[x][y] = 2 #뱀이 차지하고 있는 곳은 2로
  q = [] #뱀이 차지하고 있는 위치정보
  q.append((x,y))
  direction = 0
  time = 0
  index = 0 #회전정보 인덱스

  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    #이동했을 때 진행조건(범위 내에있고, 이동한 뱀의 머리가 뱀의 몸통과 부딪히지 않고)
    if nx >= 1 and ny >= 1 and nx <= n and ny <= n and data[nx][ny] != 2:
      #사과 유무
      #사과X
      if data[nx][ny] == 0:       
        #꼬리
        px,py = q.pop(0)
        data[px][py] = 0
      #사과O
      if data[nx][ny] == 1:
        data[nx][ny] == 2
       
    #끝날조건
    else:
      time += 1
      break

    #진행
    #이동 후 머리 설정
    x = nx
    y = ny
    q.append((x,y))
    time += 1
    #회전 총 수 l만큼 시간이 될때 마다 회전정보를 저장해놓은 Info에서 확인 
    if index < l and time == info[index][0]:
      direction = turn(direction, info[index][1])
      index += 1
  return time 

print(simulate()) 