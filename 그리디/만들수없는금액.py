#만들어야할 금액(target)과 들어오는 값 비교, target없데이트
#비슷한 문제 : 백준 2437
n = int(input())
data = list(map(int,input().split()))

data.sort()
target = 1

for i in data:
    if target < i:
        break

    target += i

print(target)
