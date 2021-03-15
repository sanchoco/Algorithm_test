# 백준 1002 터렛

import sys, math

n = int(sys.stdin.readline())

result = []
for i in range(n):
	x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
	dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

	if x1 == x2 and y1 == y2 and r1 == r2: #같을 때
		result.append(-1)
	elif dis > r1 + r2 or math.fabs(r1 - r2) > dis: # 멀거나 안에 있거나
		result.append(0)
	elif (dis + r1) == r2 or (dis + r2) == r1 or (r1 + r2) == dis:
		result.append(1)
	else:
		result.append(2)

for r in result:
	print(r)
