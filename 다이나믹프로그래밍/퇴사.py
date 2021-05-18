import sys
input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))

dp = [0]*(n+1)
for day in range(n-1,-1,-1):
    t = data[day][0]
    p = data[day][1]

    if day+t <= n: 

        dp[day] = max(p+dp[day+t],dp[day+1])
    else: 
        dp[day] = dp[day+1]


print(dp[0])

