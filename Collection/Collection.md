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
	
defaultdict # 키에 기본 값을 지정

	dfd = defaultdict(lambda: 0) # defaultdict 선언, 기본값은 0
	dfd_list = defaultdict(list) # defaultdict 선언, 기본값은 []
		
Counter # 시퀀스 자료형의 데이터 요소 개수를 딕셔너리로 반환

	c= Counter(text) # Counter 생성
	c_element= list(Counter(text).elements()) # 요소들을 리스트 형태로 만듬
	ck=Counter(red=4, blue=5) # 기본값을 설정, 단 red나 blue값은 문자열로 지정
	a = Counter(['a', 'b', 'c', 'd', 'e'])
	b = Counter(['a', 'b', 'a'])
	d = Counter(a=-4, b=1)
	e= Counter(a=-1, b=0)
	print(a+b) # Counter끼리 덧셈 가능, 단 음수와 0 값은 나오지 않음
	print(a-b) # Counter끼리 뺄셈 가능, 단 음수와 0 값은 나오지 않음
	d.subtract(a) # Counter끼리 뺄셈 가능 단 음수와 0값도 출력 단 이떄 d값이 바뀌는 구조
	print(a | e) # Counter끼리 or 연산 같은 키가 있으면 값이 큰거만 출력 음수와 0은 출력X
	print(a & e) # Counter끼리 and 연산 같은 키가 있으면 값이 작은 값 출력 음수와 0은 출력X
	
namedtuple # 이름이 있는 튜플

	
	p3d = namedtuple("p3d", "x y z") # namedtuple 선언
	p3d = namedtuple("p3d", "x, y, z")
	p3d = namedtuple("p3d", ['x', 'y', 'z'])
	
	p4d= namedtuple("p1d", "x y z") # 이런식으로는X because? 헷갈림
	
	p1 = p3d(1, 2, 3) # p1에 네임드 튜플 대입
	p3 = p3d(y=3, z=2, x=1)
	
	print(p1) # 네임드 튜플 전체 출력
	
	print(p1.x, p1.y, p1.z) # 네임드 튜플 부분 출력
	print(p1[0], p1[1], p1[2])
	
	
