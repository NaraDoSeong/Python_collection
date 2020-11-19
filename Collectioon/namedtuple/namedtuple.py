from collections import namedtuple

p3d = namedtuple("p3d", "x y z") # namedtuple 선언
"""
p3d = namedtuple("p3d", "x, y, z")
p3d = namedtuple("p3d", ['x', 'y', 'z'])
"""
p4d= namedtuple("p1d", "x y z") # 추천 X 헷갈림

p1 = p3d(1, 2, 3)  # p1에 네임드 튜플 대입
print(p1) # 네임드 튜플 전체 출력
print(p1.x, p1.y, p1.z) # 네임드 튜플 부분 출력
print(p1[0], p1[1], p1[2])

p2 = p4d(1, 2, 3)
print(p2) # p4d(1,2,3)이지만 p4d는 p1d이기에 p1d롤 출력

p3 = p3d(y=3, z=2, x=1)
print(p3)


