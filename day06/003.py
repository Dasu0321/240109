# 원시타입, 내장함수 <-> import
# 개발자는 값을 검증
#   - 우리 사이트를 공격하는 사람은 user다

# str(ing) 타입
# '': 문자열의 시작, 끝 = <p></div>
str1='10'
str2="3.14"
str3='홀짝홀짝홀짝홀짝'

# 연산
print(str1+str2) # 연결
print(str1*10)   # 반복

# 인덱스 연산 -> 시퀀스와 동일
print(str3[0]) # 홀
print(str3[5]) # 짝

# 슬라이싱(slicing)연산 -> 시퀀스와 동일
print(str3[0:3]) # 홀짝홀

str4="032123"
print(str4[0:3]) # 032
print(str4[1:])  # 32123
print(str4[::2]) # 022

str5 = "0123456789"
# 홀수만 출력 13579
print(str5[1::2])
# 3의 배수만 출력 0369
print(str5[::3])

# 내장함수 : len (용어11)
print(len('hello'))

# ☆ 문자열은 변경이 불가능하다 (innuteable <-> mutable)
str6='hello'
list6=['h','e','l','l','o']
#str6[0]='z' #답을 바꿀 수 없다
list6[0]='z' #답을 바꿀 수 있다
print(list6)
