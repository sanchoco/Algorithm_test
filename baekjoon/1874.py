stack = list()
result = list()

n = int(input())

check = True
use = 1 #push에 사용한 것 표시
for i in range(n): ## pop을 진행하는 반복
	num = int(input())
	while (use <= num): #입력받은 수까지 push 과정
		stack.append(use)
		result.append('+')
		use += 1
	if (stack[-1] == num): # 입력받은 수와 같다면 pop 진행
		stack.pop()
		result.append('-')
	else:
		check = False
if check:
	for re in result:
		print(re)
else:
	print("NO")
