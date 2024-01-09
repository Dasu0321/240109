# 숫자 타입 -> 타입마다 사용할 수 있는 연산, 함수가 다르다
# 산술연산: +,-,*,/,//,%]

# 10과 3.14 변수 ※같은 타입이면, 짧게
num1, num2 = 10, 3.14

# +,-,*,/ 결과 출력 -> 한줄로
hap = num1+num2
print(hap)
print(num1+num2)
print(f'합계 : {num1+num2}, 곱셉: {num1*num2}') # 합계에 빼기, 곱하기, 나누기 쓰면 되나?
print('합계 : {num1+num2}') # f(포맷)이 없음 문자화

num2 = 3
print(f"몫 : {num1//num2}")
print(f"나머지 :  {num1%num2}")

print(-num1)

# 함수 : 이름을 가진 기능 -> 재사용, 내장함수 (import x)
# abs -> 절댓값 (용어10)
# num1의 절댓값 출력
print(abs(-3))
print(abs(-100))
print(abs(100))