#리스트 내에서 원하는 원소의 위치 찾기
#이진탐색
#재귀함수

def binary_search(array, target, start, end):
  #원소가 존재하지 않을 때 start와 end 가 교차한 순간
  if end < start:
    return None
  #중간값을 구하고 소숫점 내림
  mid = (end + start) // 2

  if target == array[mid]:
    return mid+1
  elif target > array[mid]:
    return binary_search(array, target, mid + 1, end)
  else:
    return binary_search(array, target, start, mid-1)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print("타겟의 위치: ", result)
