str = input()

croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

count = 0
i = 0

# 문자열을 앞에서부터 없애나가는 방식

while (len(str)): # 남은 문자열의 길이가 1이상일 때
	flag = 0 # 대체할 문자를 찾았을 때 아래 실행 방지
	for c in croa:
		if (len(str) < len(c)): # 남은 str 문자열보다 대체 문자가 길 떄 스킵
			continue
		if (c == str[0:len(c)]): # 앞에 문자가 대체 문자랑 같을 때
			str = str[len(c):] # 찾은 문자 없애고 저장
			count += 1 # 찾은 수 +1
			flag = 1 # 찾았다는 표시
			break
	if flag == 0: # 찾지 못했을 경우 실행
		count += 1 # 문자 하나도 크로아티아 문자 하나에 해당
		str = str[1:] # 문자 하나 제거

print(count) #결과


