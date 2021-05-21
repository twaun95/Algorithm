# dp테이블 총 개수만큼 선언
# 바텀업을 위해 시작부분 초기화
# 로직찾기
# 범위 range
# 비교 (현재값 + dp[현재위치] , dp[비교할 index]) 주의사항 : 현재값 위치에서 전 위치의 값들을 바라봐야함!!
# 결과 : dp[현재구해야할 값 = index]
n = int(input())
dp = []
for i in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        if j == i:
            up_right = 0
        else:
            up_right = dp[i-1][j]

        dp[i][j] = max(up_left, up_right)+dp[i][j]

result = 0
for i in range(n):
    result = max(result, dp[n-1][i])
print(result)

