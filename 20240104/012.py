# 주민번호를 입력받아 성별을 출력
id_num='971012-1035112'
print(id_num[7])
if id_num[7] in ('1','3','5'):
    print('남성')
elif id_num[7] in ('2','4','6'):
    print('여성')
else:
    print('잘못된 문자입니다')




