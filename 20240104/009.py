# 1년은 몇초인지 출력
days_per_year=365
hours_per_day=24
sec_per_hour=60
sec=60
year_per_sec=days_per_year*hours_per_day*sec_per_hour*sec
print(year_per_sec)

# 45분간 일하고 10분씩 휴식. 전체 근무시간 480분이면 휴식 시간의 합계
# full_work=480
# work=45
# rest=10
# w_r=work+rest
# full_work_to_hour=full_work//w_r
# full_rest=full_work_to_hour*rest
# print(full_rest)

# 숫자를 입력받아 1의 자리까지 버리고 출력
# 예) 3512->3510, 359->350
# a=3512
# aa=a//10*10
# aaa=a-a%10
# b=359
# bb=b//10*10
# bbb=b-b%10
# print(aa)
# print(bb)
# print(aaa)
# print(bbb)

# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수
# 예) 17->14, 21->21
a=105
aa=a//7*7
print(aa)

# 자연수를 입력받아 그 숫자보다 작은 최대의 7의 배수
# 17->14,21->14
b=106
bb=(b-1)//7*7
print(bb)



