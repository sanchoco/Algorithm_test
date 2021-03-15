text = input()

num = 0
arr = []
for i in range(len(text)):
	if text[i] in "0123456789":
		num = num * 10 + int(text[i])
	else:
		arr.append(num)
		arr.append(text[i])
		num = 0
arr.append(num)

total = arr[0]
minus = 0
if len(arr) > 1:
	for i in arr[1:]:
		if i == '-':
			minus = 1
		elif i == '+':
			continue
		else:
			if minus == 0:
				total += i
			else :
				total -= i

print(total)
