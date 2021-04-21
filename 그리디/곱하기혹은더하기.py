data = list(map(int,input()))

result = data[0]

for i in range(1,len(data)):
    num = data[i]
    if result<=1 or num<=1:
        result += num
    else:
        result *= num

print(result)
