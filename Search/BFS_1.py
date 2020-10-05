from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True

  while queue:
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

#그래프의 정보를 담은 2차원리스트
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
#방문정보를 담은 리스트
visited = [False] * 9
#노드1을 시작으로하는 그래프의 BFS 탐색 시작
bfs(graph, 1, visited)