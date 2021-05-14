#https://www.acmicpc.net/problem/1932
n = int(input())
dp = []

for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0: #해당 위치 기준 위 왼쪽에서 오는 경우가 맨 왼쪽이면 0
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        
        if j == i: #해당 위치 기준 위 오른쪽에서 오는 경우가 맨 오른쪽이면 0
            up_right = 0
        else:
            up_right = dp[i-1][j]
        # 해당 테이블 값 + 위왼쪽과 위오른쪽에서 오는 값 중 큰 값
        dp[i][j] = dp[i][j] + max(up_right,up_left)

answer = 0

for i in range(n):
    answer = max(dp[n-1][i], answer)

print(answer)
