from collections import OrderedDict

# key의 값으로 정렬하기 위한 함수 t[1]로하면 value값으로 정렬
def sort_by_key(t):
    return (t[0])

od = OrderedDict() # OrderedDict을 선언

od['x'] = 400
od['y'] = 200
od['l'] = 500
od['z'] = 300

odd = OrderedDict(sorted(od.items(), key=sort_by_key))

for k, v in odd.items():
    print(k, v)
