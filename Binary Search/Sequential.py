def sequential_search(n, target, array):
  for i in range(n):
    if array[i] == tartet:
      return i+1

print("생성할 원소개수, 찾을문자 두개를 공백으로 구분하여 입력하시오")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("원소개수만큼 입력")
array = input().split()

print(sequential_search(n, taret, array))
