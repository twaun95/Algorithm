#선택정렬 예제1
array = [7,5,9,0,3,1,6,2]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  #스와프
  array[i], array[min_index] = array[min_index], array[i]

print(array)