#https://www.acmicpc.net/problem/1932
n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        
        if j == i:
            up_right = 0
        else:
            up_right = dp[i-1][j]

        dp[i][j] = dp[i][j] + max(up_right,up_left)

answer = 0

for i in range(n):
    answer = max(dp[n-1][i], answer)

print(answer)