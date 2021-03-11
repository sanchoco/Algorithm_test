import copy

def left_turn(arr): # 첫번째 원소를 가장 뒤로
	value = arr.pop(0)
	arr.append(value)
	return arr

def right_turn(arr): # 마지막 원소를 가장 앞으로
	value = arr.pop(-1)
	arr.insert(0,value)
	return arr

N, M = map(int, input().split()) # 첫 번째 줄 입력

check = list(map(int, input().split())) # 두 번째 줄 입력

arr = list(range(1, N + 1)) # 스택 생성

count = 0
for value in check:
	if value == arr[0]: # 바로 찾으면
		arr.pop(0)
	else:
		# 테스트 준비
		test1 = 0
		test1_arr = copy.deepcopy(arr)
		test2 = 0
		test2_arr = copy.deepcopy(arr)

		# 테스트
		count += 1 # 테스트 과정에서 한번 돌리고 시작하니 count를 +1
		while value != left_turn(test1_arr)[0]: # 문제의 2번 연산
			test1 += 1
		while value != right_turn(test2_arr)[0]: ##문제의 3번 연산
			test2 += 1
		count+= test1 if test1 < test2 else test2 # 왼쪽과 오른쪽 테스트 중 적은 쪽을 합산
		arr = test1_arr # test1이나 test2 둘 다 찾은 arr이니 덮어씌움
		arr.pop(0)
print(count)






