str = list(input().upper()) # 입력
check = list(0 for i in range(ord('Z') - ord('A') + 1)) #배열을 저장할 리스트 생성

for c in str: # 리스트에 저장
	check[ord(c) - ord('A')] += 1 # 해당 문자에 맞는 리스트 자리에 +1 카운트
count = 0
c = ''
for i in range(len(check)):
	if check[i] == max(check): # 가장 자주 나온 문자의 수
		count += 1 # count가 2가 넘어가면 중복이므로 c = ?
		c = chr(i + ord('A'))

if count != 1 : # 중복이 있을 떄
	print('?')
else :
	print(c)

