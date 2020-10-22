# Python_collection
Collection module

deque # 스택과 큐 자료구조 제공, 연결 리스트의 특성을 지원

    from collections import deque
    dq_list = deque() # dg_list = deque([]) # deque를 선언 
	dq_list.append(1)
	dq_list[0] # 인덱싱 기능 지원
	# dq_list[0:1] # 슬라이싱 기능 지원 X


deque_stack # 선입 후출(FILO: First In Last Out)

	dq_list.append() # 넣기
	dq_list.pop() # 빼기
	

deque_queue # 선입 선출(FIFO: First In First Out)

	#case 1:
	dq_list.appendleft() # 넣기
	dq_list.pop() # 빼기
	
	#case 2:
	dq_list.append() # 넣기
	dq_list.popleft() # 빼기

		
