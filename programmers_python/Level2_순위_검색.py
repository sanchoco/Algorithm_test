# 프로그래머스 Level2 순위 검색
# 정확성 통과 효용성 실패

def solution(info, query):
	answer = []

	#parcing 딕셔너리 사용
	person_dic = {}
	for d1 in ['-','cpp','java','python']:
		for d2 in ['-', 'backend', 'frontend']:
			for d3 in ['-', 'junior', 'senior']:
				for d4 in ['-', 'chicken', 'pizza']:
					person_dic[str(d1+d2+d3+d4)] = []

	for i in info:
		person = i.split()
		score = int(person[4])
		for d1 in ['-', person[0]]:
			for d2 in ['-', person[1]]:
				for d3 in ['-', person[2]]:
					for d4 in ['-', person[3]]:
						person_dic[str(d1+d2+d3+d4)] = person_dic[str(d1+d2+d3+d4)] + [score]

	for q in query:
		case = q.split(' and ')
		food, score =  case[3].split()
		case[3] = food
		case.append(int(score))
		st = str(case[0] + case[1] + case[2] + case[3])
		find = 0
		for i in person_dic[st]:
			if i >= case[4]:
				find += 1
		answer.append(find)

	############

	# 처음 풀었을 때
	# persons = []
	# for i in info:
	# 	person = i.split()
	# 	person[4] = int(person[4])
	# 	persons.append(person)

	# 	# 지원자 탐색
	# for q in query:
	# 	case = q.split(' and ')
	# 	food, score = case[3].split()
	# 	case[3] = food
	# 	case.append(int(score))
	# 	find = 0
	# 	for person in persons:
	# 		if ((case[0] == '-') or (person[0] == case[0])) \
	# 		and ((case[1] == '-') or (person[1] == case[1])) \
	# 		and ((case[2] == '-') or (person[2] == case[2])) \
	# 		and ((case[3] == '-') or (person[3] == case[3])) \
	# 		and ((case[4] == '-') or (person[4] >= case[4])):
	# 			find += 1
	# 	answer.append(find)

	return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
		"cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
		 "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info, query))
