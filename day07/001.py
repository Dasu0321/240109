# 웹프로그래밍의
# 데이터 1건 : dictionary (용어1)
# 여러건 : list (용어2)
# 데이터 모델링

# 키와 값의 pair -> spring/25 (용어3)
info = {"아이디":'spring', '나이':'25', '성인여부':"True"}
print(info)

# 책 pair -> 아심미/안정광/15,560   일련번호 : (끝자리) ※고객은 의미 유무x
#   -> 딕셔너리로 list를 만든다
book1 = {"제목":'아빠가 심리학자라 미안해', '저자':'안정광', '가격':15560}
print(book1)
book2 = {'번호':'7887728', '제목':"아빠가 심리학자라 미안해", '출판사':"책사람집",
        '저자':'안정광', '출판일자':"2023-10-13", '가격':"15560", '할인여부': "False"}
print(book2)
products =[
    {'번호':1, '이름':'코카콜라', '가격':2000, '재고':20},
    {'번호':2, '이름':'펩시', '가격':1900,'재고':10}
]
print(products[0]['이름'])