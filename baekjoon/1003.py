
table = [-1] * 41 # -1로 채운 테이블 0번부터 40번까지의 테이블
# 더 깊이 안들어가고 fibo(0)과 fibo(1)의 실행 횟수 결과를 담아두고 재사용

def fibonacci(n): # 함수 시작
	if (table[n] != -1): # 이미 테이블에 결과가 있을 경우 참조하여 리턴
		return table[n]
	if (n == 0):
		table[0] = [1, 0] # fibo(0)에서 0의 횟수는 1, fibo(1)의 횟수는 0을 저장
		return table[0] # 결과 저장
	if (n == 1): # fibo(0)에서 0의 횟수는 0, fibo(1)의 횟수는 1을 저장
		table[1] = [0, 1]
		return table[1] # 1에 해당하는 테이블 리턴
	else:
		first = fibonacci(n-1) #fibo(n-1) 연산
		second = fibonacci(n-2) #fibo(n-2) 연산
		a = first[0] + second[0] # 앞의 결과로 나온 fibo(0)실행 개수 결과 합산
		b = first[1] + second[1] # 앞의 결과로 나온 fibo(1) 실행 개수의 결과 합산
		table[n] = [a, b] # 테이블에 fibo(n)의 결과를 n번째에 저장
		return [a, b] # 결과 리턴

result = [] # 결과 저장

#입력
n = int(input())
for i in range(n):
	num = int(input())
	out = fibonacci(num) # 0과 1호출의 결과
	result.append(out)

for r in result:
	print(r[0], r[1])
