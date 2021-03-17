# 백준 1753 최단경로
import sys
from heapq import heappop, heappush

INF = float("inf")

V, E = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline())
route = {}
cost = [INF] * (V + 1)
for _ in range(E):
	u, v, w = map(int, sys.stdin.readline().split())
	if u in route:
		route[u] += [(v, w)]
	else :
		route[u] = [(v, w)]

visit = []
heappush(visit, (0,start))
cost[start] = 0
while visit:
	value, node = heappop(visit)
	if node in route:
		for v, w in route[node]:
			if cost[v] > value + w: # 이전 비용 > 경유 직전 비용 + 경유지에서 목적지의 비용
				cost[v] = value + w # 탐색후 작은 값으로 업데이트
				heappush(visit,(cost[v], v))

for i in range(1, V + 1):
	if cost[i] == INF:
		print("INF")
	else:
		print(cost[i])
