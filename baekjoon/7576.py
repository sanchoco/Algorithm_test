import sys
from collections import deque

# 준비
dx = [-1,1,0,0] # dx[0]dy[0]과 같이 상하좌우 토마토를 확인할 때 시용
dy = [0,0,-1,1]
start_node = deque() # 큐를 사용해야 하기 때문에 deque 사용
table = [] # 토마토 박스

# 입력
M, N = map(int, sys.stdin.readline().split())
for i in range(N):
	table.append(list(map(int, sys.stdin.readline().split())))

#BFS
# 순서
# 1. 시작전부터 1인 익은 토마토를 작업 목록(큐)에 넣음
# 2. 작업 목록(while queue)에 있으면 상하좌우를 확인(for i in rage(4))
# 2. 상하좌우 중 안익은 토마토(0)이 있으면 현재 토마토보다 +1값을 부여하여 익힘
# 3. 2에서 익힌 토마토를 작업 목록(큐)에 추가
# 4. 작업 목록에 남아 있는지 확인(2로 돌아가서 반복)

##토마토 익히는 과정 옆 토마토는 기준 토마토의 +1값을 가짐
def tomato(array, start_node):
	queue = start_node # 시작 전 1인 토마토를 받아 큐에 저장
	while queue:  # 작업해야 할 것이 남아 있다면
		position = queue.popleft()  # 작업해야 할 위치를 작업 목록에서 뽑아 옴
	 	##!! 아래 주석을 지우고 동작 과정을 확인할 수 있음!
		# print("작업 기준 위치: ", position[1], position[0])
		# for st in array:
		# 	print(st)
		for i in range(4):  # dx,dy를 사용하여 상하좌우 탐색!
			x = position[1] + dx[i] # 작업 목록 기준 i가 돌면서 상하좌우 가르킴
			y = position[0] + dy[i]
			if 0 <= x < M and 0 <= y < N and array[y][x] == 0: # 탐색해야 하는 위치의 올바른 위치이고 안익은 토마토(0)인 경우
				array[y][x] = array[position[0]][position[1]] + 1 # 기준 위치보다 +1된 값을 저장
				queue.append([y, x])  # 주위를 탐색해야 할 대상으로 큐에 저장

# 1인 토마토를 찾아 시작 큐에 넣기
for i in range(N):
	for j in range(M):
		if table[i][j] == 1:
			start_node.append([i, j])

# 실행
tomato(table, start_node)

# 토마토 날짜와 안 익은게 있는지 확인, 최대 일수 확인
day = 0
for i in table:
	for j in i:
		if j == 0: # 안 익은 토마토가 있다면 day를 -1로 바꾸고 break
			day = -1
			break
		elif day < j - 1:
			day = j - 1
	if j == 0: # 위에 break에서 빠져나올 떄 여기서도 빠져냐오기 위함
		break

# 결과 출력
print(day)
