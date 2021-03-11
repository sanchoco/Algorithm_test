a = int(input())
b = int(input())

line1 = a * (b % 10) # 1의 자리
line2 = a * (int((b % 100)/10)) # 10의 자리: 100으로 나눈 나머지를 10으로 나눈 몫
line3 = a * int(b / 100) # 100의 자리는 100으로 나눈 몫
line4 = a * b

print(line1)
print(line2)
print(line3)
print(line4)
