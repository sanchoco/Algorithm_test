case = int(input())
data = []
for i in range(case):
	temp = list(map(int,input().split()))
	data.append(temp)

for i in range(case):
	count = 0
	avg = sum(data[i][1:])/data[i][0]
	for j in data[i][1:]:
		if avg < j :
			count += 1
	result = count / data[i][0] * 100
	print(str(format(result,".3f")) + "%")

