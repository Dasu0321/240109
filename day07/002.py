todos = [
    {"tno":1, "title":"자바공부", "finish": False},
    {"tno":3, "title":"파이썬공부", "finish": False}
]

# Create (용어4)
tno = 4
title = input('할일 입력:')
todo = {"tno":tno,"title":title,"finish":False}
todos.append(todo)
tno = tno+1
print(todos)
print(tno)

# Read : for로 todos 출력 (용어5)
for todo in todos :
    print(todo)

# Update : tno로 todoes를 찾아 finish를 toggle (용어6)
#          못 찾으면 아무것도 하지 않는다
input_tno = int(input('변경할 할 일 번호:'))
for todo in todos:
    if todo['tno'] == input_tno:
        todo['finish'] = not todo['finish']
        break
print(todos)

# Delete : 입력한 tno에 해당하는 todo를 todos에 찾는다 (용어6)
# 
input_tno = int(input('삭제할 할 일 번호 입력:'))
for todo in todos:
    if todo['tno'] == input_tno:
        todos.remove(todo)
        break

print(todos)