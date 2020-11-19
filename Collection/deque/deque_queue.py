
from collections import deque

dq_list = deque()

# case 1:
for i in range(6):
    dq_list.appendleft(i) # 넣기
print(dq_list)

dq_list.pop() # 빼기
print(dq_list)

dq_list=deque()
# case 2:
for i in range(6):
    dq_list.append(i) # 넣기
print(dq_list)

dq_list.popleft() # 빼기
print(dq_list)
