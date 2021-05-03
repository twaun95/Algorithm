#https://www.acmicpc.net/problem/18310
import sys
input = sys.stdin.readline

n = int(input())
home = list(map(int,input().split()))

home.sort()
#중간값이 결국 정답 
#-1은 짝수일 때, 가장 작은값 출력을 위해
print(home[n//2 -1])
