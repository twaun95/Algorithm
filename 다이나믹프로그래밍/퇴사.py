#https://www.acmicpc.net/problem/14501
#https://jrc-park.tistory.com/119?category=378936
import sys

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

dp = [0]*(n+1)
for day in range(n-1,-1,-1): #거꾸로
    t = data[day][0]
    p = data[day][1]

    if day+t <= n: #이동 가능한 날짜일 때
        # p(현재)+이동했을때의 값 vs 앞의값
        dp[day] = max(p+dp[day+t],dp[day+1])
    else: #이동 가능 범위가 벗어났으면 값 유지
        dp[day] = dp[day+1]

print(dp[0])

