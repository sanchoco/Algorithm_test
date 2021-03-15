# 백준 2579 계단 오르기

# import sys

# arr = [0] * 301
# score = [0] * 301

# n = int(sys.stdin.readline())
# for i in range(n):
# 	arr[i] = int(sys.stdin.readline())

# score[0] = arr[0]
# score[1] = arr[0] + arr[1]
# score[2] = max(arr[1] + arr[2], arr[0] + arr[2])

# for i in range(3,n):
# 	score[i] = arr[i] + max(score[i - 3] + arr[i - 1], score[i - 2])

# print(score[n-1])
