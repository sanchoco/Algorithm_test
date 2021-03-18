# 프로그래머스 Level2 문자열 압축

def solution(s):
	answer = 9999
	if len(s) == 1: # 문자가 하나일 경우
		return 1
	for i in range(1,len(s)//2+1): # 길이의 절반까지 쪼개보기
		lst = []
		for j in range(0, len(s), i): # 문자열을 i개 단위로 나눠서 리스트 저장
			lst.append(s[j:j+i])
		before = lst[0] # 이전 문자와 비교
		count = 1 # 이전 문자와 중복해서 나온 경우 카운트
		temp = "" # 압축 결과를 담을 임시 변수
		for index in range(1, len(lst)): # 리스트 인덱스 1번부터
			if before == lst[index]: #이전 단어와 같은 경우
				count += 1
			else : # 앞의 단위와 다르다면,
				if count == 1: # 중복되지 않은 경우
					temp += before #이전의 단위 그대로 temp에 담기
				else : # count가 올라가서 여러개가 있는 경우
					temp += str(count) + before # 압축숫자와 이전 문자열 담아주기
				before = lst[index] # 현재 단위를 이전 단위로 설정
				count = 1 # 카운트 초기화
		if count == 1: #마지막 문자 담기
			temp += before
		else :
			temp += str(count) + before
		answer = min(answer, len(temp)) # 가장 좋은 압축길이로 갱신
	return answer

s = input()
print(solution(s))
