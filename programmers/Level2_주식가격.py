# 프로그래머스 Level2 주식가격

def solution(prices):
	n = len(prices)
	answer = [0] * n # n개의 결과 저장
	for i in range(n): # 기준 시간부터 끝까지 반복
		for j in range(i+1,n): #비교 시간이 늘어날수록
			answer[i] += 1 # 1초 증가
			if prices[i] > prices[j]: #만약 기준 시간의 가격보다 비교 시간의 가격이 작으면
				break # 멈춤
	return answer


#테스트
prices = [1, 2, 3, 2, 3]
print(solution(prices))

# prices = [6,5,4,3,2,1]
# print(solution(prices))
