# 백준 2164 카드2
from collections import deque

n = int(input())

cards = deque(range(1, n + 1))

last = 0
while cards:
	last = cards.popleft()
	if cards:
		temp = cards.popleft()
		cards.append(temp)

print(last)
