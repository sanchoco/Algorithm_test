# 백준 2231 분해합
n = int(input())
result = 0
for num in range(n):
	value = num
	original = num
	while num != 0:
		value += num % 10
		num = num // 10
	if value == n:
		result = original
		break

print(result)
