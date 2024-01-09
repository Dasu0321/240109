# numbers = []
# while True:
#     print("|======= 메뉴 선택 =======|")
#     print("(1: 추가, 2: 합계 3: 평균, 4: 삭제, 999: 종료)")
#     select = input("번호 입력")
#     if select == '1':
#         num = int(input('숫자 입력'))
#         numbers.append(num)
#     elif select == '2':
#         print (f'합계 : {sum(numbers)})')
#     elif select == '3':
#         print (f'평균 : {sum(numbers)/len(numbers)}')
#     elif select == '4':
#         val = int(input("삭제할 값 입력:"))
#         if val in numbers:
#             numbers.remove(val)
#     elif select == '999':
#         print('이용해주셔서 감사합니다')
#         break

numbers = []
while True:
    print ("1.추가 2.출력 3.합계 4.값으로 삭제 999.종료")
    select = input('메뉴 선택')
    if select == '1':
        val = int(input('숫자 입력'))
        numbers.append(val)
    elif select == '2':
        for number in numbers:
            print(number, end = " ")
        print()
    elif select == '3':
        print(f'합계:{sum(numbers)}')
    elif select == '4':
        value = int(input('삭제할 숫자:'))
        if value in numbers:
            numbers.remove(value)
    elif select == '999':
        print('이용해주셔서 감사합니다')