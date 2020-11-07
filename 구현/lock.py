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

def ext_key(key):
  n = len(key)
  m = len(key[0])
  
  result = [[0] * n*3 for _ in range(m*3)]
  for i in range(n):
    for j in range(m):
      result[i+m][j+m] = key[i][j]
  return result

print(ext_key(test))
"""
def check(key,lock):
  while
  lock을 ext_key내에서 찾기!
  찾으면 True, break
  없으면 false
"""
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