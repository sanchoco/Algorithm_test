a, b, v = map(int, input().split()) # 올라갈 떄, 잘 때, 최종 목표

day = (v - b) // (a - b) # 잠들기 전 도착 미터 / 하루에 오를 수 있는 미터
if (((v - b) % (a - b)) > 0): # 나머지가 나올 경우 하루에 오르지 못함
	day += 1

print(int(day))
