def self_num(num):
	temp = 0 # num의 각 자리가 더해질 임시 변수, 아래 cp_num의 마지막 숫자가 여기 더해짐
	cp_num = num # 각자리를 더할 떄 쓰일 변수 1234 -> 123 12 1 0
	while (True):
		temp += cp_num % 10
		if cp_num == 0:
			break
		cp_num = cp_num // 10
	return (num + temp)

num = list() #셀프넘버가 아닌 수 저장
for i in range(10001): # 0~10000까지 돌면서 셀프넘버가 아닌 숫자들 모두 저장
	num.append(self_num(i))

for i in range(10001):
	if i not in num: # 저장되지 않은 수만 출력
		print(i)


