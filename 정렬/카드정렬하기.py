import heapq
import sys
input=sys.stdin.readline

n = int(input())
card=[]
for _ in range(n):
    heapq.heappush(card,int(input()))

result = 0
while len(card)>1:
    A = heapq.heappop(card)
    B = heapq.heappop(card)
    heapq.heappush(card, A+B)
    result += A+B

print(result)