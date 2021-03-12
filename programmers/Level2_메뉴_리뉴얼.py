#프로그래머스 Level2 메뉴 리뉴얼

from itertools import combinations

def solution(orders, course):
	answer = [] # 정답을 담을 배열
	cases = [] # 모든 문자 조합을 담을 리스트
	fav = {} # 좋아하는 구성의 자주 나온 횟수를 담은 딕셔너리

	for menus in orders: #가장 많이 찾는 메뉴를 딕셔너리에 저장
		menus = ''.join(sorted(menus)) # "YX" -> "XY"와 같이 문자열 정렬
		for c in course:
			cases += list(map(''.join, combinations(menus, c))) # 코스의 숫자대로 문자 조합

	for case in cases: # 구성과 자주 나온 횟수를 fav딕셔너리에 담음
		if case not in fav:
			fav[case] = 1 # 아직 나온 적 없는 조합이라면 횟수를 1로 설정
		else:
			fav[case] += 1 # 한번 이상 나왔으면 횟수 +1

	for c in course: # 코스 숫자대로 조회
		high = 0 # 가장 많이 나온 횟수
		arr = [] # 나중에 결과 값에 더해줄 임시 리스트
		for f in fav.items():
			if (len(f[0]) == c) and (f[1] >= 2): # 2회 이상 나오고 현재 코스 숫자와 같을 때
				if f[1] > high: # 가장 많이 나온 요리인 경우
					high = f[1] # 많이 나온 요리 갱신
					arr = [str(f[0])]
				elif f[1] == high: # 숫자가 동률인 경우
					arr += [str(f[0])] # 이 세트 메뉴 조합도 추가
		answer += arr # 현재 세트 갯수의 많이 나온 조합을 추가

	answer.sort() # 알파벳 순 정렬
	return answer


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# course = [2, 3, 4]

# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# course = [2,3,5]

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

print(solution(orders, course))
