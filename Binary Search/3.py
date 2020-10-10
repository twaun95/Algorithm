#계수 정렬 이용

n = int(input())
# 모든 범위만큼 배열 지정
array = [0] * 1000000

# 가게에 존재하는 부품 번호는 1로
for i in input().split():
  array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
  if array[i] == 1:
    print('yes', end=' ')
  else:
    print('no', end=' ')