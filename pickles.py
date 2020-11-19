import pickle

# 객체 써넣기
f = open("list.pkle", "wb")
lst = [1, 2, 3, 4, 5]
pickle.dump(lst, f)
f.close()

# 객체 읽어 오기
f = open("list.pkle", "rb")
answer=pickle.load(f)
print(answer)
f.close()

class Multiply(object):
    def __init__(self, multiplier):
        self.multiplier = multiplier
    def mult(self, num):
        return num * self.multiplier

mobj = Multiply(100)
print(mobj.mult(5))


f = open("Multiply.pkle", "wb")
pickle.dump(mobj, f)
f.close()

f = open ("Multiply.pkle", "rb")
mobj_saved = pickle.load(f)
print(mobj_saved.mult(100))