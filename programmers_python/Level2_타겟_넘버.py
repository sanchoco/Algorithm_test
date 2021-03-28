# 프로그래머스 Level2 타겟 넘버

def dfs(numbers, target, depth, total):
	if depth == len(numbers):
		if target == total:
			return 1
		else :
			return 0
	result = 0
	result += dfs(numbers, target, depth + 1, total + numbers[depth])
	result += dfs(numbers, target, depth + 1, total + (-1 * numbers[depth]))
	return result

def solution(numbers, target):
	answer = 0
	answer = dfs(numbers, target, 0, 0)
	return answer

num = [1, 1, 1, 1, 1]
target = 3
print(solution(num,target))
