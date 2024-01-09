# 파이썬은 타입을 바꿀 수 있고 파이썬이 알아서 바꾸는 경우도 있다
# int, float, str, bool, (list,set,diction)
# 타입을 바꾸는 함수는 타입의 이름과 같다
'3'
print(int('3'))

# '3'을 정수로 바꾼 다음 타입을 확인해보자
# '3'을 print(int('3'))을 통해 정수로 바꿔줬다 -> '3'이라는 문자열이 3이됨
# 3이라는 정수를 print(type(int('3')))을 통해 3을 정수로 출력하게 만듦
# int(), type(), print()
print(type(int('3')))

# 6이 나오게 수정 3+'3'
print(3+int('3'))

# 3+'3.14'를 출력(6.14)
print(3+float('3.14'))
print(float("3.14")+3)
# 실수(float)는 근사값이라 계산식에는 정확한 값이 나올 수 없다(정확한 값이 나올 수도 있고 아닐 수도 있다)

#'55'
print('5'+'5')
print('5'+str(5))
print('당신은 성인입니까?'+str(True))
