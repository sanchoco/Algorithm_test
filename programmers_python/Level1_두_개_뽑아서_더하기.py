# 프로그래머스 Level1 두 개 뽑아서 더하기

def solution(numbers):
	answer = [] # 정답 저장
	size = len(numbers) # numbers의 길이
	for i in range(size): #기준 숫자의 인덱스
		for j in range(i + 1, size): # 비교할 숫자의 인덱스
			answer.append(numbers[i] + numbers[j])
	answer = sorted(list(set(answer))) # 중복 제거 및 정렬

	return answer

# 테스트
numbers = [2, 1, 3, 4, 1]
print(solution(numbers))
