# 프로그래머스 Level2 프린터

def solution(priorities, location):
	n = len(priorities)
	for i in range(n): # 로케이션 기억
		if i == location: # 출력 원하는 문서를 1로 기억
			priorities[i] = [priorities[i], 1]
		else:
			priorities[i] = [priorities[i],0] # 아닌 문서들은 0으로 세팅

	turn = 1
	while True:
		importance = max(priorities)[0] # 가장 높은 우선 순위인 값
		if priorities[0][0] == importance: # 가장 높은 우선 순위인 경우
			if priorities[0][1] == 1: # 출력해야 하는 문서일 경우
				return turn # 리턴
			else: #가장 높은 우선 순위지만 원하는 문서가 아닐 경우
				priorities[0][0] = 0 # 중요도를 0으로 변경
				priorities.append(priorities.pop(0)) # 값을 맨 뒤로
				turn += 1 # 인쇄 횟수 1
		else :
			priorities.append(priorities.pop(0)) # 문서 순서를 뒤로 보내기

#테스트
# priorities = [2, 1, 3, 2]
# location = 2
# print(solution(priorities, location))

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
