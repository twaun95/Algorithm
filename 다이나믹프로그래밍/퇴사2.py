N = int(input())

T = []
P = []
for i in range(N):
    a, b = map(int, input().split(' '))
    T.append(a)
    P.append(b)

dp = [0 for _ in range(N+2)]

for i in range(N):
    if dp[i] > dp[i+1]:
        dp[i+1] = dp[i]

    if i + T[i] <= N:
        if dp[i + T[i]] < P[i] + dp[i]:
            dp[i + T[i]] = P[i] + dp[i]

print(dp)