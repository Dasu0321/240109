# 할 일 관리
todos = [
    {'tno':1, 'tile':'할 일1', 'reg_day':'2024-01-09', 'finish':False},
    {'tno':2, 'tile':'할 일2', 'reg_day':'2024-01-09', 'finish':False},
    {'tno':3, 'tile':'할 일3', 'reg_day':'2024-01-09', 'finish':False}
]
tno = 2


# Read : 전체읽기, 1개읽기
찾았니 = False
for todo in todos:
    print(todo)

# 할 일 번호를 입력받아 찾아서 출력
input_tno = int(input('할 일 번호 입력:'))
for todo in todos:
    if todo['tno'] == input_tno:
        print(todo)
        찾았니 = True
        break
if 찾았니 == False:
    print('할 일을 찾을 수 없습니다')