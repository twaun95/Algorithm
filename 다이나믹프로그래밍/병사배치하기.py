#각 지점에 대해서 조건을 만족하는 최장길이 구한 후
#최대값이 만들 수 있는 가장 긴 길이
#LIS알고리즘

n = int(input())
data = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[j] > data[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
