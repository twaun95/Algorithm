#재귀함수를 이용한 dfs 구현

def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

#2차원 리스트
graph = [
  [],           #graph[0]
  [2,3,8],      #graph[1]
  [1,7],        #graph[2]
  [1,4,5],      #graph[3]
  [3,5],        #graph[4]
  [3,4],        #graph[5]
  [7],          #graph[6]
  [2,6,8],      #graph[7]
  [1,7]         #graph[8]
]

#방문정보 확인 리스트
visited = [False] * 9

# 노드1부터 시작하는 dfs 함수 호출
dfs(graph, 1, visited)