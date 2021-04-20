#리스트 내에서 원하는 원소의 위치 찾기
#이진탐색
#반복문

def binary_search(array, target, start, end):
  #원소가 존재하지 않을 때 start와 end 가 교차한 순간
  while start <= end:
    mid = (end + start) // 2

    if target == array[mid]:
      return mid+1
    elif target > array[mid]:
      start = mid +1
    else:
      end = mid-1

  #반목문이 끝났을 때 == 원소가 존재하지 않을 때
  return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print("타겟의 위치: ", result)
