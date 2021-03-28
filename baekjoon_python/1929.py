import math

# 에라토스테네스의 체 사용
def isPrime(num):
	if num == 1:
		return False
	for i in range(2,int(math.sqrt(num) + 1)): ## 제곱근까지 확인
		if (num % i) == 0:
			return False
	return True

a, b = map(int, input().split())
for i in range(a, b + 1):
	if isPrime(i):
		print(i)

