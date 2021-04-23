#https://www.acmicpc.net/problem/15686
#총 도시개수에서 M개만큼 짝을 지어 도시의 치킨 거리를 구하고 이들 중 최소값
#1.총 도시 개수에서 m개 좌표만 남기기 (select)
#2. m개의 좌표에 대해 각각의 치킨거리 구하고 더하기 (sum chick len)
#3. 최소 도시의 치킨거리 구하기 = answer
from itertools import combinations
INF = 987654321

n, m = map(int,input().split())
data = []
for i in range(n):
    data.append(list(map(int,input().split())))

def find_citychicklen(all_store,all_city):#해당 조합에서 총 도시 치킨거리
    length = INF # 각 도시의 치킨거리 -> 각 시티마타 가게까지의 최소거리 
    all_length = 0 # 총 도시치킨거리 -> 각 도시의 length를 합한 값 

    for city in all_city:
        for store in all_store:
            length = min(abs(store[0]-city[0]) + abs(store[1]-city[1]), length)
        all_length += length
        length = INF   

    return all_length

city = []
store = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            city.append([i,j])
        elif data[i][j] == 2:
            store.append([i,j])

answer = INF
for cn in combinations(store,m):
    answer = min(answer, find_citychicklen(cn, city))#각 조합에서의 도시의치킨거리의 최소값 찾기

print(answer)
