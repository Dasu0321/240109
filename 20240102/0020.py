# 초를 입력받아 몇분 몇초인지 출력
# ex) 210초라고 입력하면 3분 30초
# sec1=int(input('초:'))
# min=sec1//60
# sec2=sec1%60
# print(f'{min}분 {sec2}초')

# 분과 초를 입력하면 초를 출력하시오
# 5분 10초 310초
min=int(input('분:'))
sec=int(input('초:'))
# 상수는 대문자로 표시
SECONDS_PER_MINUTE=60
sec2=(min*SECONDS_PER_MINUTE)+sec
print(f'{sec2}초')

# 코드에 값이 직접 나타나는 것 : literal

