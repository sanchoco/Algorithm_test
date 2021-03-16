# 백준 11054 가장 긴 바이토닉 부분 수열

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

left_start = [1] * n
for i in range(n):
	value = arr[i]
	for j in range(i):
		if arr[j] < value:
			left_start[i] = max(left_start[i], left_start[j] + 1)

right_start = [1] * n
for i in range(n - 1, 0, -1):
	value = arr[i]
	for j in range(n - 1, i, -1):
		if arr[j] < value:
			right_start[i] = max(right_start[i], right_start[j] + 1)
max_len = 0
for i in range(n):
	max_len = max(max_len, left_start[i] + right_start[i] - 1)

print(max_len)
