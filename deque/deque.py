from collections import deque

dq_list = deque() # dg_list = deque([])

for i in range(5):
    dq_list.append(i)
print(dq_list)

print(dq_list[0])
# print(dq_list[1:2]) 슬라이싱 기능 지원 X

dq_list.rotate() # 한칸씩 뒷자리로 이동 맨 마지막은 처음으로 이동
print(dq_list)
dq_list.appendleft(dq_list.pop()) # 맨마지막 수를 맨 앞으로 이동
print(dq_list)

print(deque(reversed(dq_list))) # 데이터를 역순으로 출력

dq_list.extend([6,7,8]) # 오른쪽으로 데이터 넣기,append와 비슷
print(dq_list)

dq_list.extendleft([6,7,8]) # 왼쪽으로 데이터 넣기, 8이 0번째, 7이 1번째, 6은 2번째
print(dq_list)

