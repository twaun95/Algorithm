#부품찾기
"""
태완이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다. 동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
"""
"""


"""

def binary_search(target, array, start, end):
  if start > end:
    return None
  
  mid = (start + end) // 2

  if target == array[mid]:
    return target
  elif target < array[mid]:
    return binary_search(target, array, start, mid-1)
  else:
    return binary_search(target, array, mid+1, end)
  
N = int(input())
array = list(map(int, input().split()))
M = int(input())
target_array = list(map(int, input().split()))

array. sort()

for i in target_array:
  result = binary_search(i, array, 0, N-1)
  if result == None:
    print("no", end = ' ')
  else:
    print("yes", end = ' ')
