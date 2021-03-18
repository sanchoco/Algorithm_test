# 프로그래머스 Level2 전화번호 목록
def solution(phone_book):
	answer = True
	phone_book.sort()
	for i in range(len(phone_book) - 1):
		if phone_book[i + 1].startswith(phone_book[i], 0):
			return False
	return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
