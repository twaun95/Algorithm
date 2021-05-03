#https://www.acmicpc.net/problem/18310
import sys
input = sys.stdin.readline

n = int(input())
home = list(map(int,input().split()))

home.sort()
print(home[n//2 -1])