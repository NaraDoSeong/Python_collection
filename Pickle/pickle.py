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
