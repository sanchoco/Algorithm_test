open_b = ['(','[']
close_b = [')',']']
par = {'(':')','[':']'}

lines = list()

while True: # 입력
	line = input()
	if line == ".":
		break;
	else:
		lines.append(line) #리스트에 저장

for line in lines: # 한줄씩 반복
	stack = []
	error = 0
	for c in line: # 한 문자씩 반복
		if c in open_b: # 여는 괄호인 경우
			stack.append(c)
		elif c in close_b: # 닫는 괄호인 경우
			if len(stack) == 0: ## 닫는 괄호 나왔는데 스택이 빈 경우 에러
				error = 1
				break
			temp = stack.pop()
			if par.get(temp) == c: # 짝이 맞을 경우 그대로 진행
				continue
			else: # 아니면 에러
				error = 1
				break

	if error == 0 and len(stack) == 0: # 문장이 끝나고 스택이 빈 경우만 yes
		print("yes")
	else:
		print("no")
