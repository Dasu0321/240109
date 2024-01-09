# 섭씨를 입력받아 화씨로 출력하시오
# (섭씨x9/5)+32=화씨
# ccs=int(input('섭씨:'))
# fh=(ccs*9/5)+32
# print(f'섭씨가 {ccs}°C일 때 화씨는 {fh}°F 입니다.')

# 온도와 종류를 입력받으시오
# ex) 온도:35
# ex) 종류:섭씨
# 종류가 섭씨면 온도를 화씨로 변환 출력, 아니면 섭씨로 변환 출력
# (화씨 − 32) × 5/9 = 섭씨


# 3.섭씨 또는 화씨를 입력받는다 -> kind
# 4.kind가 섭씨면 화씨로 변환
f=int(input('온도:'))
ccs1=f
fh=(ccs1*9/5)+32
ccs2=(fh-32)*5/9
if ccs1==f:
    print(f'섭씨 {ccs1}는 화씨 {fh}')
else:
    print(f'섭씨는 {ccs2}')

temp=int(input('온도 입력:'))
kind=input('현재 온도 종류(섭씨 또는 화씨) 입력:')
if kind=='섭씨':
    화씨변경
else:
    섭씨변경