# bool
# and: 모두 다 참이어야 한다
# or: 하나만 참이면 된다
b1, b2, b3, b4 = True, True, True, False
print(b1 and b2 and b3)
print(b1 and b2 and b4)
print(b4 and b1 and b2)
print(b1 or b2 or b4)
print((b4 and b1) or (b4 or b1))
# print(b1 and b2 and b4) < print(b4 and b1 and b2)

nai = 24
gender = '여자'
city = '인천'
# 나이가 20이상이고 성별은 여자
nai>=20 and gender == '여자'
# (나이가 20이상이고 성별은 여자인 사람) 또는 인천에 사는 사람
#  - 조건 2개
(nai>=20 and gender == '여자') or city =='인천'

print("=====================")
print(5>3 + 10>7)