# 프로그래머스 Level1 완주하지_못한_선수

def solution(participant, completion):
	participant.sort()
	completion.sort()
	answer = ''
	for i in range(len(participant)):
		if len(completion) <= i or participant[i] != completion[i]:
			answer = participant[i]
			break
	return answer


participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
result = solution(participant, completion)
print(result)
