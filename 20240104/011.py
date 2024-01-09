# 길이를 입력받아 센티미터 또는 인치로 변환해 출력한다.
# 길이가 양수인 경우 인치로 변환, 음수인 경우 센티미터로 변환
length=int(input('길이:'))
cm_to_inch=length/2.54
inch_to_cm=length*2.54
if length>0:
    print(f'{cm_to_inch}inch')
else:
    print(f'{inch_to_cm}cm')
# 길이=25
# if 길이>0:
#   결과=str(길이/2.54)+'인치'
# else:
#   결과=str(길이*2.54)+'cm'
# print(결과)


# scope : 변수를 사용할 수 있는 범위
# 블록이 스코프를 생성하는 언어:Java
# 함수가 스코프를 생성하는 언어:Python
# 둘 다 되는 언어:Java Script

