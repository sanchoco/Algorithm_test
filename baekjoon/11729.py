arr = []
def hanoi(n, go, to, sub): # 판 남은 개수, 출발핀, 목적핀, 보조핀
	if n == 1:
		arr.append(go + ' ' + to) # 가장 큰 판을 목적지로 보낸 메세지 저장  ex) 1->3
	else: # 2개 이상일 때
		hanoi(n-1, go, sub, to) # 가장 큰 판을 빼고 보조로 보냄 ex)1->2
		arr.append(go + ' ' + to) # 가장 큰 판을 목적지로 보낸 것을 출력
		hanoi(n-1, sub, to, go) #보조로 보낸 (가장 큰 판 제외한 판들)을 목적지로 옮기기 ex) 2->3

n = int(input()) #입력
hanoi(n, '1','3','2') #하노이 함수 시작

print(len(arr))
for string in arr:
	print(string)
