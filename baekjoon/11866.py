# 백준 11866 요세푸스 문제 0

from collections import deque



queue = deque()

n,k = map(int, input().split())

for i in range(1, n + 1):
	queue.append(i)

result = []
while queue:
	for i in range(k):
		queue.append(queue.popleft())
	result.append(queue.pop())

print("<", end='')
print(str(result).replace('[','').replace(']',''), end='')
print(">")
