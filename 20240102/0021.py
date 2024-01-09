# 몇일인지 입력받아 몇개월 며칠인지 출력
# 333일 - 11개월 3일
DAYS_PER_MONTH=30
days1=int(input('일수:'))
month=days1//DAYS_PER_MONTH
days2=days1%30
if days2<=0:
    print(f'{month}개월')
else:
    print(f'{month}개월 {days2}일')