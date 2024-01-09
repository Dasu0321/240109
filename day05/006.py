list1 = [1,3,5]

# 10 in list1 : 결과가 참거짓(10이 list1에 있니?)

# list의 원소를 하나씩 꺼내 item에 담는 반복문
for item in list1:
    print(item)

index=0
while index<3:
    print(list1[index])
    index+=1

# break : 반복문을 중단한다
while True:
    a = int(input('값을 입력하세요(999면 종료)'))
    if a==999:
        break
    print(f'입력한 값 : {a}')