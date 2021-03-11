num = int(input())

v1 = 0
v2 = 0
count = 0
success = num

while(True):
	v1 = num // 10 # 4
	v2 = num % 10 # 7
	num = (v2 * 10) + ((v1 + v2) % 10)
	count += 1
	if (success == num):
		break

print(count)


