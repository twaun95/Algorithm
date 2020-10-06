#계수정렬 예제1

array = [4,1,6,2,0,3,3,0,2,1,8]

count = [0] * (max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end=' ')