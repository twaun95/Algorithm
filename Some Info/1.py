Alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# 공백으로 구분하여 특정 개수를 입력받기
n,m,k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받고 리스트에 저장
data = list(map(int, input().split()))

# 리스트의 오름차순, 내림차순
data = [3, 1, 2]
data.sort()
data.sort(reverse = True)

# 대문자, 소문자 변형

# for반복문
for i in data:
  print(i)

for i in range(3): # 0~2
  print(i)

for i in range(0,3): # 0~2
  print(i)