import sys

# 입력
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 이전 기록 저장
result = [1] * n #숫자 위치에 따른 최대 증가수열 길이를 저장하는 배열, 이전 값 활용을 위한 DP

for i in range(n): # 기준점이 되는 반복문
	for j in range(i): # 비교 대상이 되는 반복문
		#만약 기준 대상(i)이 비교대상(j)보다 크고 비교대상의 증가수열(result)이 더 긴 경우
		if arr[j] < arr[i] and result[i] <= result[j]:
				result[i] = result[j] + 1 #해당 숫자 위치의 증가수열 결과로 저장

print(max(result))

##### 설명 ######
# 예시로 6개 수열 10 30 20 40 50 30 이 들어왔을 때
# 결과를 담는 result 배열도 1  1  1  1  1  1로 세팅되어 있습니다.
# 1. 10(i:0)은 처음이기에 앞에 숫자가 없어 10까지의 최대 증가 수열은 1입니다.
#		j는 range(0)이기 때문에 돌지 않습니다. result[0]은 그대로 1
# 2. 30(i:1)은 range(1)이기 때문에 j:0으로 한번 반복하며 arr[0]인 10과 비교합니다.
#		30이 더 크므로 arr[0]의 결과인 result[0]을 살펴보고 같거나 크므로 1을 증가시킨 값인 2를 result[1]에 저장합니다.
# 현재 result는 1 2 1 1 1 1 !!!!
# 3. 20(i:2)은 j in range(2)이기 때문에 반복문을 통해 arr[0](10)과 arr[1](30)을 살펴보게 됩니다.
#		반복 중 현재 기준인 20과 비교 대상인 10(j:0)을 비교하고 result도 같기 때문에
# 		10의 결과(result[0])1을 증가한 값을 20의 결과(result[2]=2)로 저장합니다.
# 4. 40(i:3)을 기준으로 배열의 앞인 10, 30, 20과 비교를 합니다.
#		10(j:0)과 비교 후 result[3](40의 결과) = result[0](10의 결과) + 1 => (2)를 저장하고
#		30(j:1)과 비교 후 result[3](40의 결과) = result[1](30의 결과) + 1 => (3)으로 저장(교체)하고
#		20(j:2)과 비교하지만 뒷 부분의 조건(result[i:3](=3) < result[2](=2))에 걸려 실행되지 않습니다.
# 현재 result는 1 2 2 3 1 1 !!!!
# 5. 50(i:4)을 기준으로 배열의 앞인 10, 30, 20, 40과 비교를 합니다.
#		4번의 아래와 동일한 과정을 거치고 40(j:3)과 비교를 합니다.
#		기준인 50과 40을 비교할 때 더 크고 result[4](=3)와 과 result[3](=3)비교하여 같거나 큰 조건에 해당하므로
#		result[4]에 result[3](=3) + 1인 4를 담습니다.
# 현재 result는 1 2 2 3 4 1 !!!!
# 6. 30(i:5)은 또 10 30 20 40 50과 비교합니다.
#		30은 30보다 작은 10(j:0)과 20(j:2)만 조건에 걸릴 것 입니다.
#		result[5]에는 10(j:0)의 결과값 1에 +1인 2가 저장되고 20(j:2)의 결과값 2에서 +1된 3이 저장될 것 입니다..
# !최종적으로 result는 1 2 2 3 4 3 !!!!
# 여기서 가장 긴 수열은 4에 해당하므로 4가 출력되어야 합니다. (10 20 40 50 또는 10 30 40 50)
