n = int(input())

dp = [0] * n
dp[0] = 1

id2 = 0#2의배수 index 
id3 = 0#3의배수 index
id5 = 0#5의배수 index

next2 = 2 #2의 배수 값
next3 = 3 #3의 배수 값
next5 = 5 #5의 배수 값
#dp배열을 채워나가면서 순서대로 2,3,5를 곱해나가며 next값들을 바꿔줌 -> 2,3,5만을 소인수로 가지는 값들이 생김

for i in range (1,n):
    dp[i] = min(next2,next3,next5)
    #(2,3,5) (4,3,5) (4,6,5) (6,6,5) (6,6,10) (8,9,10)....
    #2, 3, 4, 5,6
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

