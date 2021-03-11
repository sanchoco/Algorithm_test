test = int(input())

arr = []
floor =0
for i in range(test):
	H, W, N = map(int, input().split())
	if (N % H == 0): # 꼭대기 층일 떄
		floor = H # 6층에 6번째 손님일 때 6층
		ho = N // H # 1호
	else :
		floor = N % H # 6층에 7번째 손님일 때 7%6 -> 1층
		ho = N // H + 1 # 201호
	arr.append(floor * 100 + ho)

for p in arr:
	print(p)
