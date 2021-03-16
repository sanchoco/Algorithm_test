# 백준 1753 최단경로
import sys, heapq

INF = 999
# 입력
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
cost = [INF] * (v + 1)
route = [[] for _ in range(v+1)]
heap = []

#실행
def di(start):
	cost[start] = 0
	heapq.heappush(heap, (0, start))
	while heap:
		value, now = heapq.heappop(heap)
		if cost[now] < value:
			continue
		for node_cost, next_node in route[now]:
			if node_cost + value < cost[next_node]:
				cost[next_node] = node_cost + value
				heapq.heappush(heap, (node_cost + value, next_node))


for _ in range(e):
	node, target, value = map(int, input().split())
	route[node].append((target, value))

# 출력
for i in range(1,v + 1):
	if cost[i] == INF:
		print("INF")
	else:
		print(cost[i])
