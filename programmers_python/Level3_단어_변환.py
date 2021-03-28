# 프로그래머스 Level3 단어 변환

def dfs(begin, target, words, depth):
	if begin == target:
		global value
		value = min(value, depth)
		return
	if target not in words:
		return
	for w in words:
		diff = 0
		for i in range(len(begin)):
			if begin[i] != w[i]:
				diff += 1
			if diff >= 2:
				break
		if diff >= 2:
			continue
		else :
			words.remove(w)
			dfs(w, target, words, depth+1)
			words.append(w)

def solution(begin, target, words):
	global value
	value = 99
	dfs(begin, target, words, 0)
	answer = value
	if value == 99:
		answer = 0
	return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

result = solution(begin, target, words)
print(result)
