# 백준 9663 N-Queen

def queen(table, n, table_length):
	global count
	for i in range(table_length):
		if check(table, n - 1, i, table_length) == True:
			if n+1 == table_length:
				count += 1
				break
			table[n][i] = 1
			queen(table, n + 1, table_length)
			table[n][i] = 0

def check(table, n, now, table_length):
	mid = now
	side = 1
	while 0 <= n:
		if table[n][mid] == 1:
			return False
		if (mid - side) >= 0 and table[n][mid-side] == 1:
			return False
		if (mid + side) < table_length and table[n][mid+side] == 1:
			return False
		n -= 1
		side += 1
	return True
global count
count = 0
table_length = int(input())
# table = [[0] * table_length] * table_length # 엄청난 실수
table = list()
for i in range(table_length):
	table.append([0] * table_length)

queen(table, 0, table_length)
print(count)
