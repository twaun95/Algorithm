# 큰 수의 법칙을 수학적 아이디어를 이용해 더 효율적으로
n,m,k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k
count += m%(k+1)

result = 0
result += (count)*first
result += (m-count)*second

print(result)