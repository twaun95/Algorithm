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
            
            if j == 0:
                left_up = 0
            else:
                left_up = dp[j-1][i-1]
         
            left = dp[j][i-1]
            
            if j == n-1:
                left_down = 0
            else:
                left_down = dp[j+1][i-1]
           
            dp[j][i] = max(left_up, left_down, left) + dp[j][i]

    answer = 0

    for i in range(n):
        answer = max(dp[i][m-1],answer)

    print(answer)


