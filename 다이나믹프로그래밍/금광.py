t = int(input())
for tt in range(t):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    dp = []
    step = 0

    for i in range(n):
        dp.append(array[step:step+m])
        step += m
    print(dp)

    for i in range(1,m):
        for j in range(n):
            #1.왼위, 범위 벗어나면 -> [0][?]일때 0
            if j == 0:
                left_up = 0
            else:
                left_up = dp[j-1][i-1]
            #2.왼쪽, 범위 벗어나면 0
            left = dp[j][i-1]
            #3.왼아래, 범위 벗어나면 -> [n-1][?]일때0
            if j == n-1:
                left_down = 0
            else:
                left_down = dp[j+1][i-1]
            #위 3개 최대값에 현재값 더한 값으로 갱신
            dp[j][i] = max(left_up, left_down, left) + dp[j][i]

    answer = 0

    for i in range(n):
        answer = max(dp[i][m-1],answer)

    print(answer)


