# 프로그래머스 Level3 여행경로
import copy

def dfs(tickets, airport):
	global answer, visited
	visited.append(airport) # 방문 공항에 추가
	if not tickets: # 티켓을 다 썼을 경우
		answer.append(copy.deepcopy(visited)) # 성공 리스트에 저장
		visited.pop() # 방문 공항에서 제거
		return 0
	for i in range(len(tickets)): # 티켓
		if tickets[i][0] == airport: # 현재 공항과 티켓 출발지가 같은 경우
			temp = tickets[i] # 티켓 정보 저장
			del tickets[i] # 티켓 삭제
			dfs(tickets, temp[1])
			tickets.insert(i,temp) # 티켓 다시 추가
	visited.pop() # 방문 공항에서 제거

def solution(tickets):
	global answer, visited
	answer = []
	visited = [] # 방문 순서를 담는 변수
	dfs(tickets, "ICN")
	answer.sort()

	return answer[0]


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], [
	"SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
result = solution(tickets)
print(result)
