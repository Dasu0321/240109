# 국어 점수 75, 80, 70이라는 국어 점수가 있다 -> 집합 타입(sequence)
# 값 하나를 저장 : int, float, str, bool
# 값 여러개를 저장 : list, tuple, dictionary, set

# kor=[75,80,70]
# print(type(kor))
# print(kor[0])
# print(kor[1])
# print(kor[2])

# 조건문, 반복문
# for 변수 in kor : kor 리스트의 원소를 하나씩 꺼내서 변수에 담는다.
kor=[75,80,70]
for item in kor:
    print(item)

# list는 변경 가능하고, tuple은 변경 불가능
# CRUD=Create,Read,Update,Delete
# 프로그램에서 CRUD 작업만 가능하다

# 리스트=["사과","귤","수박"]
# 튜플=("사과","귤","수박")
리스트=["사과","귤","수박"]
튜플=("사과","귤","수박")
for list in 리스트:
    print(list)
for tuple in 튜플:
    print(tuple)



