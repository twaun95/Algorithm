import sys
input = sys.stdin.readline

n, x = map(int,input().split())
data = list(map(int,input().split()))

def find_start(data, target, start, end):
    if start > end:
        return -1

    mid = (start+end) // 2
    if data[mid] == target:
        if data[mid-1] != target:
            return mid
        else:
            return find_start(data, target, start, mid-1)
    elif data[mid] > target:
        return find_start(data, target, start, mid-1)
    else:
        return find_start(data, target, mid+1, end)

def find_end(data, target, start, end):
    if start > end:
        return -1

    mid = (start+end) // 2
    if data[mid] == target:
        if data[mid+1] != target:
            return mid
        else:
            return find_end(data, target, mid+1, end)
    elif data[mid] > target:
        return find_end(data, target, start, mid-1)
    else:
        return find_end(data, target, mid+1, end)


startIdx = find_start(data, x, 0, n-1)
if startIdx == -1:
    print(-1)
else:
    endIdx = find_end(data, x, startIdx, n-1)
    print(endIdx-startIdx+1)

