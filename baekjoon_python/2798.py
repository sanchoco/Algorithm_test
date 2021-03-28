# 백준 2798 블랙잭
import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(n):
	for j in range(i + 1, n):
		for k in range(j + 1, n):
			if m < cards[i]+cards[j]+cards[k]:
				continue
			result = max(result, cards[i]+cards[j]+cards[k])

print(result)
