# 프로그래머스 Level3 네트워크

def dfs(n, computers, start, group, net):
	if net[start] != 0: # 이미 탐색했다면,
		return
	net[start] = group # 탐색 표시와 그룹 넘버 설정
	for i in range(n):
		if computers[start][i] == 1 and net[i] == 0:
			dfs(n, computers, i, group, net)

def solution(n, computers):
	for i in range(n): # 네트워크 그래프 합치기
		for j in range(n):
			if i != j and computers[i][j] == 1:
				computers[i] = computers[j] = [max(x,y) for x, y in zip(computers[i], computers[j])]
	group = 1
	net = [0] * n
	for i in range(n):
		dfs(n, computers, i, group, net)
		group += 1
	print(computers)
	answer = len(set(net))
	return answer

# n = 3
# com = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# n = 3
# com = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

n = 5
com = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [
	0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]

print(solution(n, com))

