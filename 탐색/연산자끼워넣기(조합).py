#https://www.acmicpc.net/problem/14888
from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
op_num = list(map(int,input().split()))

op = ['+','-','*','/']
op_all = []#각 연산자의 개수만큼 총 리스트
for i in range(4):
    op_all.extend(op[i]*op_num[i])

#연산자 조합 리스트
op_permutation = set(permutations(op_all,n-1))

min_sum = 10**9  #10억
max_sum = -10**9 #-10억
for oper in op_permutation:
    result = data[0]
    for i in range(n-1):
        if oper[i] == '+':
            result += data[i+1]
        elif oper[i] == '-':
            result -= data[i+1]
        elif oper[i] == '*':
            result *= data[i+1]
        elif oper[i] == '/':
            if result < 0:
                result = -((-result) // data[i+1])
            else:
                result //= data[i+1]
    
    min_sum = min(min_sum, result)
    max_sum = max(max_sum, result)

print(max_sum)
print(min_sum)
