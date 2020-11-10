#2020 카카오 신입 공채
#https://programmers.co.kr/learn/courses/30/lessons/60059
"""
고고학자인 튜브는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 그런데 문을 열러고 살펴보니 특이한 형태의 자물쇠로 잠겨 있었고 문 앞에는 특이한 형태의 열쇠와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해주는 종이가 발견되었습니다.
잠겨있는 자물쇠는 격자 한 칸의 크기가 1x1의 NxN 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 MxM 크기의 정사각 격자 형태로 되어 있습니다. 
자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안 됩니다. 또한 자물쇠의 모든 홈을 채워 비워있는 곳이 없어야 자물쇠를 열 수 있습니다.
열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열 수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.
"""
"""
*제한사항
- key는 MxM(3<= M <= 20, M은 자연수) 크기 2차원 배열입니다.
- lock은 NxN(3<= N <= 20, N은 자연수) 크기 2차원 배열입니다.
- M은 항상 N이하입니다.
- key와 lock의 원소는 0 또는 1로 이루어져 있습니다. 이때 0은 홈 부분, 1은 돌기 부분을 나타냅니다.
"""

test = [[1,1,1],[1,1,1],[1,1,1]]

def rotated(key):
  n = len(key)
  m = len(key[0])

  result = [[0] * n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = key[i][j]
  return result

print(rotated(test))

def ext_lock(lock):
  n = len(lock)
  m = len(lock[0])
  
  result = [[0] * n*3 for _ in range(m*3)]
  for i in range(n):
    for j in range(m):
      result[i+m][j+m] = lock[i][j]
  return result

print(ext_lock(test))

#lock이 모두 1인지 check
def check(lock):
  n = len(lock)//3
  m = len(lock[0])//3
  result = 1

  for i in range(n,2*n):
    for j in range(m,2*m):
      result *= lock[i][j]

  return result
print(check(ext_lock(test)))


def solution(key, lock):
  
  lock = ext_lock(lock)
  answer = True
  n = len(lock)

  for _ in range(4):
    key = rotated(key)
    #덧셈
    for: 세로
      for: 가로
        for: n만큼
          newlock = key(움직이는 key) + lock(고정)
          if check(newlock) == 1:
            return answer

  answer = False

  return answer

"""
def up(a):
  n = len(a)
  m = len(a[0])

  result = [[0] * n for _ in range(m)]
  for i in range(n-1):
    for j in range(m):
      result[i][j] = a[i+1][j]
  return result

print(up(test))

def down(a):
  n = len(a)
  m = len(a[0])

  result = [[0] * n for _ in range(m)]
  for i in range(1,n):
    for j in range(m):
      result[i][j] = a[i-1][j]
  
  return result
print(down(test))

def right(a):
  n = len(a)
  m = len(a[0])

  result = [[0] * n for _ in range(m)]
  for i in range(n):
    for j in range(1,m):
      result[i][j] = a[i][j-1]
  
  return result
print(right(test))

def left(a):
  n = len(a)
  m = len(a[0])

  result = [[0] * n for _ in range(m)]
  for i in range(n):
    for j in range(m-1):
      result[i][j] = a[i][j+1]
  
  return result
print(left(test))
"""