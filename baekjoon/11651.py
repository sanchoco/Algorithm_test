arr = list()

n = int(input())

for i in range(n):
	x, y = map(int, input().split())
	arr.append([y, x]) # y부터 정렬 필요

arr.sort()
for a in arr:
	print(a[1], a[0])
