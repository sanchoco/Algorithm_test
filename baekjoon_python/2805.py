import sys

def cut(trees, mid): # 함수 캐싱 문제로 백준 사이트 시간초과로 따로 빼냄
        total = 0
        for tree in trees:
                if tree > mid:
                        total += tree - mid
        return total


N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(trees)

val = 0 # 결과 저장
# 이진 탐색
while start <= end : #start와 end가 역전될 때 까지
	total = 0
	mid = (start + end) // 2
	total = cut(trees, mid)
	if total >= M: #자른 결과가 목표랑 같거나 클 때 -> 너무 많이 잘림
		val = mid # 결과 저장
		start = mid + 1 # 절단기 높이 올리기, 절단기 높이를 올려야 자를 때 덜 잘림
	else: # 목표보다 덜 잘렸을 때
		end = mid - 1 # 절단기 높이를 낮춰서 많이 잘리게 하고 탐색

print(val)
