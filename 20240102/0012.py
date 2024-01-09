# 함수 : 이름을 가진 코드 덩어리
# print, type, int, float, str (bool(강제로 bool로 바꾸는 것은 의미 없음))

print(type(5+3))
print(max(3,4))
a=max(3,4)
print(a)

print(min(10,20))
b=min(10,20)
print(b)

# sum 함수는 sum([])형태로 쓰임
# iterable - 값의 집합이 와야한다는 의미의 에러메세지
print(sum([10,20,30]))

print(max(3,7,10))
print(max(70,60,sum([100,200])))
print(sum([max(5,80,50),min(100,20,60)]))

print(max([1,2,3]))
print(min([1,2,3]))

print(max(3,7)+10)
print(sum([max(3,7),10]))