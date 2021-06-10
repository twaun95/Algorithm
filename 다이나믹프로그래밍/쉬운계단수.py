#    0 1 2 3 4 5 6 7 8 9
# n
# 1  0 1 1 1 1 1 1 1 1 1
# 2  1 1 2 2 2 2 2 2 2 1 
# 3  1 3 3 4 4 4 4 4 3 2

# 2차원 표에서 해당 수가 될 경우는 전단계(n-1)에서 해당수 +1, 해당수-1에서 올 경우.
# 단 0이 될 경우는 1에서 오는 것만 가능, 9가 될 경우는 8에서 오는 것만 가능

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
