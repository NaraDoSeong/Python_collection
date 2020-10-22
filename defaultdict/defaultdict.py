from collections import defaultdict

dfd = defaultdict(lambda: 0) # defaultdict 선언, 기본값은 0

print(dfd['First']) # 기본값인 0 출력

s = [('x', 1), ('y', 2), ('x', 3), ('y', 4), ('z', 5)]
dfd_s= defaultdict(list)

for k, v in s:
    dfd_s[k].append(v)

print(dfd_s.items())
print(dfd_s['a']) # 새로운 값 입력
print(dfd_s.items()) # 새로운 값은 기본값을 가진 상태로 자료형에 같이 들어감
print(dfd_s['a'])
