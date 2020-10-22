# Python_collection
Collection module

deque # 스택과 큐 자료구조 제공, 연결 리스트의 특성을 지원

    from collections import deque
    dq_list = deque() # dg_list = deque([]) # deque를 선언 
	dq_list.append(1)
	dq_list[0] # 인덱싱 기능 지원
	# dq_list[0:1] # 슬라이싱 기능 지원 X
	dq_list.rotate() # 한칸씩 뒷자리로 이동 맨 마지막은 처음으로 이동, 인자의 기본값 1
	dq_list.appendleft(dq_list.pop()) # 맨마지막 수를 맨 앞으로 이동
	print(deque(reversed(dq_list))) # 데이터를 역순으로 출력
	dq_list.extend([6,7,8]) # 오른쪽으로 데이터 넣기,append와 비슷
	dq_list.extendleft([6,7,8]) # 왼쪽으로 데이터 넣기, 8이 0번째, 7이 1번째, 6은 2번째
	
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

	
OrderedDict # 순서가 있는 딕셔너리


	od = OrderedDict() # OrderedDict을 선언
		
