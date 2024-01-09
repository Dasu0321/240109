# 함수, 변수 -> 이름을 가진다 -> 재사용하기 위함
# 변수는 쉽고 알아보기 좋아야 재사용하기 유용함

# 이름은 알아보기 쉽게, 소문자, _로 만든다(Python)
# SumOfAllScores=220 -> C
# sumOfAllScores=220 -> Java
# sum_of_all_scores=220 -> Python
sum_of_all_scores=220

# 키워드(예약어)는 사용할 수 없다
# 파이썬이 사용하는 단어 : 예약어
# 파라미터 +는 단순 합치기
# 파라미터 ,는 띄어쓰기 포함한 합치기

# 당신의 이름을 변수에 저장하시오
my_name='서준우'
print(my_name)
my_age=29
# 제 이름은
print('제 이름은',my_name,'입니다.')

# 나이를 1증가시킨다음 "나이는 23"이라고 출력
my_age=my_age+1
print('나이는',my_age,'살')

your_dog_name_is_choco='초코'
print('우리집 강아지 이름은',your_dog_name_is_choco+'에요')
print(your_dog_name_is_choco+'는 산책을 아주 좋아해요')

w_g=3000000
print('급여 :',w_g)
print('급여 : '+str(w_g))

sam_ele=78500
all_stock_price=sam_ele*10
print('10주의 총 평가금액은',all_stock_price,'원 입니다.')
print('10주의 총 평가금액은 '+str(all_stock_price)+' 원 입니다.')