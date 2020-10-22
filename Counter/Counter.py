from collections import Counter

text= list("Yellow")

c= Counter(text) # Counter 생성
print(c)
print(c['l'])

c_element= list(Counter(text).elements()) # 요소들을 리스트 형태로 만듬
print(c_element)

ck=Counter(red=4, blue=5) # 기본값을 설정, 단 red나 blue값은 문자열로 지정
print(ck)
print(list(ck.elements()))

print("\n")
a = Counter(['a', 'b', 'c', 'd', 'e'])
b = Counter(['a', 'b', 'a'])

print(a+b) # Counter끼리 덧셈 가능  단 음수와 0 값은 나오지 않음
print(a-b) # Counter끼리 뺄셈 가능  단 음수와 0 값은 나오지 않음

d = Counter(a=-4, b=1)
e= Counter(a=-1, b=0)
print(a+d)

d.subtract(a) # Counter끼리 뺄셈 가능 단 음수와 0값도 출력
print(d)


print(a | e) # Counter끼리 or 연산 같은 키가 있으면 값이 큰거만 출력
print(a & e) # Counter끼리 and 연산 같은 키가 있으면 값이 작은 값 출력 음수와 0은 출력X
print(e|d)