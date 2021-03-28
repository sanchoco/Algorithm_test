# 입력
N = int(input()) # 상근이의 카드 수
cards = list(map(int, input().split())) # 카드 리스트
cards.sort()  # 카드 정렬
M = int(input()) # 찾아야 할 카드의 수
finds = list(map(int, input().split())) #찾아야 할 카드 리스트

result = list()  # 결과 값을 담을 리스트
for num in finds: # 찾아야 하는 숫자를 하나씩 끄집어 냄
	start, end = 0, len(cards) - 1 # 탐색해야 할 범위
	find = False # 찾았을 때 True
	# 이분 탐색
	while start <= end: # 카드 인덱스의 범위
		mid = (start + end) // 2
		if cards[mid] < num: #만약 찾을 수보다 크면 위쪽 범위
			start = mid + 1
		elif cards[mid] > num:  # 만약 찾을 수보다 작다면 아랫쪽 범위
			end = mid - 1
		else :
			find = True
			break;
	if find:
		result.append('1')
	else :
		result.append('0')
print(' '.join(result))
