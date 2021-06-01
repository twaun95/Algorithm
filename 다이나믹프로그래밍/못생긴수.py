n = int(input())

dp = [0] * n
dp[0] = 1

id2 = 0#2의배수 index 
id3 = 0#3의배수 index
id5 = 0#5의배수 index

next2 = 2 #2의 배수 값
next3 = 3 #3의 배수 값
next5 = 5 #5의 배수 값

for i in range (1,n):
    dp[i] = min(next2,next3,next5)
    
    if dp[i] == next2:
        id2 += 1#다음 2의 배수값을 설정
        next2 = 2*(dp[id2])
    if dp[i] == next3:
        id3 += 1#다음 3의 배수값을 설정
        next3 = 3*(dp[id3])
    if dp[i] == next5:
        id5 += 1
        next5 = 5*(dp[id5])

print(dp[n-1])

