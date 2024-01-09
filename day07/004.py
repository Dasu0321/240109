numbers = [1,3,5,7]

# 그 숫자가 numbers에 있는 지(True/False) 출력
# 한 번만 찾으면 성공, 실패는 numbers의 모든 값에 대해서 못 찼았어야 한다
# 성공과 실패의 조건이 다르다 -> if ~ else ~ 가 아니다
# 디자인 패턴
num = 55
isFind = False
for item in numbers:
    if item==num:
        print(True)
        isFind= True
if isFind == False:
        print(False)
else:
        print(True)
