# 레벤슈타인 거리 - 두 문장 비교.
# 처음 초기값 str1(세로)에서 str2(가로)이 되기 위한 작업.
# 1. 다르다면 왼, 오른, 대각에서 가장 작은값 +1 
#   1-1. 왼쪽이면 하나를 삽입하는 것이 최소
#   1-2. 위면 하나를 삭제하는 것이 최소
#   1-3. 대각이면 변경하는 것이 최소
# 2. 같다면 대각 값 그대로(비교하는 두개의 전값과 동일)
str1 = input()
str2 = input()

n = len(str1)
m = len(str2)

dp = [[0]*(m+1) for _ in range(n+1)]

#첫 값들은 비교를 할 수 없기에 초기화 i는 해당 값을 삭제해야 같아지기 때문에 위의값에 +1
for i in range(1,n+1):
    dp[i][0] = i
for j in range(1,m+1):
    dp[0][j] = j

for i in range(1, n+1): #초기화 해줬기 때문에 1 부터
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1 #왼,대각, 위

print(dp[i][j])
