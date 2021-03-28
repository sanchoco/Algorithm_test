# 프로그래머스 Level2 기능개발

def solution(progresses, speeds):
	answer = [] # 결과물 저장
	days = 0
	while days <= 100:  # 하루 1% 씩 최대 100일까지 증가
		finished = 0 # 완료 작업물
		i = 0 # 작업 반복
		while i < len(progresses): # 작업 돌면서 진도 증가
			progresses[i] += speeds[i] # 작업 게이지 올리기
			if progresses[i] >= 100 and i == 0: #앞의 작업이 100%가 넘어서 완료될 경우
				finished += 1 # 작업 완료 개수 누적
				progresses.pop(0) # 작업 완료
				speeds.pop(0) # 작업 완료
				i = 0 # 다음 작업이 인덱스 0번이기 때문에 확인하기 위해 0으로 세팅
				continue
			i += 1
		if finished > 0: #하루에 작업 완료된 것 스택에 넣기
			answer.append(finished)
		days += 1
		if not progresses:
			return answer
	return answer


#테스트 1 => [1, 2, 3]
# progresses = [40, 93, 30, 55, 60, 65]
# speeds = [60, 1, 30, 5, 10, 7]

#테스트 2 => [2, 1]
# progresses = [93, 30, 50]
# speeds = [1, 30, 5]

#테스트 3 => [1, 3, 2]
# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

#테스트 4 => [1, 2]
# progresses = [100,98,98]
# speeds = [1,1,1]

#테스트 5 => [2, 4]
progresses = [93, 30, 55, 60, 40, 65]
speeds = [1, 30, 5 , 10, 60, 7]

print(solution(progresses, speeds))
