#https://www.acmicpc.net/problem/10825
import sys
input = sys.stdin.readline

n = int(input())
student = []
for i in range(n):
    student.append(input().split())

sorted_student = sorted(student, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(sorted_student[i][0])
