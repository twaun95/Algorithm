import heapq
import sys
input=sys.stdin.readline

n = int(input())
card=[]
for _ in range(n):
    heapq.heappush(card,int(input()))

result = 0 #결과(출력값)
while len(card)>1:
    A = heapq.heappop(card) #제일 작은 카드 HEAP에서 빼기
    B = heapq.heappop(card) #그 다음 작은 카드 HEAP에서 빼기
    heapq.heappush(card, A+B) # A,B합치고 다시 HEAP에 넣기
    result += A+B #결과 - 두 값을 계속 더하는 값

print(result)
