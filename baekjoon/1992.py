# 백준 1992 쿼드트리

def check_zero(table, n, x, y):
	for i in range(x, x+n):
		for j in range(y, y+n):
			if table[i][j] == 1:
				return False
	return True


def check_one(table, n, x, y):
	for i in range(x, x+n):
		for j in range(y, y+n):
			if table[i][j] == 0:
				return False
	return True


def half(table, n, x, y):
	if check_zero(table, n, x, y):
		return "0"
	if check_one(table, n, x, y):
		return "1"
	n = n//2
	result = ""
	result += half(table, n, x, y)
	result += half(table, n, x, y + n)
	result += half(table, n, x + n, y)
	result += half(table, n, x + n, y + n)
	return "("+result+")"


# 입력
n = int(input())
table = []
for i in range(n):
	table.append(list(map(int, (list(input())))))

#실행
result = half(table, n, 0, 0)

print(result)

