a='34'
b=int(a)
c=float(a)
d=str(b)

# ar을 튜플로 변환해 br에 저장하시오
ar=[30,40,50]
br=tuple(ar)

# 리스트에 원소를 추가한다 : append
# .은 멤버 연산자(Java기준)
# append는 독립된 함수가 아니라 ar에 소속된 함수 -> method
# method : 독립된 함수가 아니라 어딘가에 소속된 함수(소속되어야만 작동함)
ar.append(1000)
print(ar)
ar.insert(2,45)
print(ar)

# xr에 40을 추가한 다음 출력하시오
xr=(10,20,30)
xr=list(xr)
xr.append(40)
xr=tuple(xr)
print(xr)

