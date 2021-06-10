n = int(input())

dp = []
dp = [[0]*10 for _ in range(n)]

for j in range(1,10):
    dp[0][j]= 1

for i in range(1, n): #단계==n
    for j in range(1, 9): #해당수
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]

result = 0
for i in range(10):
    result += dp[n-1][i]

print(result % 1000000000)