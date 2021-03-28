a,b = input().split()

a = int(a)
b = int(b)

if (b < 45): # 분이 45분 미만이면 시를 줄여야 함
	if (a == 0): # 0시 일경우
		a = 23 # 23시로 만듬
	else:
		a = a - 1 #시에서 1을 뺌
	b = b + 60 #시에서 가져온 것을 분에 더하기
b = b - 45 # 45분 일찍

print(a, b)
