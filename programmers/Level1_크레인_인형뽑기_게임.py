# 프로그래머스 Level1 크레인 인형뽑기 게임

def solution(board, moves):
	answer = 0
	before = 0 # 이전 인형 기억
	size = len(board) # 보드 사이즈
	dolls = [] #뽑은 인형 목록담는 리스트
	for m in moves: # 움직임 한번 마다
		m -= 1 # 움직임은 1부터지만 테이블은 0부터이므로 -1로 맞춰줌
		for i in range(size): # 테이블에서 한칸씩 크레인 내리기
			if (board[i][m]) != 0: #빈곳(0)이 아닌 곳을 찾으면
				if before == board[i][m]: # 이전에 뽑았던 인형이랑 같으면
					board[i][m] = 0 #뽑은 자리를 비움(0으로)
					dolls.pop() # 같은 인형이 연달아 나왔으므로 인형 목록에서 하나 제거
					answer += 2 # 방금 뽑은 인형이랑 이전에 뽑은 인형을 터트려야 하므로 +2 카운트
					before = 0 #이전에 뽑은 인형을 0으로 초기화
					if dolls: # 만약 뽑은 인형 목록이 존재한다면(비어있지 않다면)
						before = dolls.pop() # 잠깐 꺼내서 이전 인형으로 기억
						dolls.append(before) # 다시 넣기
					break
				else: # 이전에 뽑은 인형이랑 같지 않다면
					dolls.append(board[i][m]) #뽑은 인형 목록에 추가
					before = board[i][m] #직전에 뽑은 인형으로 등록
					board[i][m] = 0 # 뽑았으니 그 자리를 비움(0으로)
					break
	return answer

# 테스트
board = [
	[0, 0, 0, 0, 0],
	[0, 0, 1, 0, 3],
	[0, 2, 5, 0, 1],
	[4, 2, 4, 4, 2],
	[3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
