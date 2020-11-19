import os

print(os.getcwd()) # 햔제 위치
print(os.listdir()) # 햔재 위치에 있는 폴더와 파일
# os.mkdir() # 폴더 생성
# os.rmdir() # 폴더 삭제
# os.chdir() # 현재 위치 이동
os.chdir('../')
print(os.getcwd())

os.path.exists("") # 존재하는지 확인
