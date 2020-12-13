# openpyxl
from openpyxl import Workbook

기본

    wb = Workbook() # 워크북 열기
    wb.save("sample.xlsx") # 저장
    wb.close() # 닫기    
    wb.sheetnames # 모든 Sheet 이름 리스트 형으로 반환
    
    from openpyxl import load_workbook
    wb = load_workbook("Samples.xlsx") # Samples.xlsx 파일을 읽어옴
    
Sheet

    ws1 = wb.active # 현재 활성화된 sheet 가져옴
    ws1.title = "sheet1" # Sheet 이름 변경
    ws = wb.create_sheet() # 새로운 기본 이름으로 생성
    ws.sheet_properties.tabColor = "000000" #RGB 형태로 탭 색 변경
    ws3 = wb.create_sheet("Test_Sheet3") # 주어진 이름으로 Sheet 생성
    ws2 = wb.create_sheet("Test_Sheet2", 2) # index에 Sheet 생성
    new_ws = wb["Test_Sheet2"] # Dict 형태로 Sheet에 접근
    target = wb.copy_worksheet(new_ws) # new_ws Sheet 복사
    
Value

    ws["locate"] = value # locate안에는 위치 A1, A2의 값을 넣고 value에는 입력할 값을 넣는다.
    ws.cell(row, column, value= value) == (ws["locate"] = value)
    ws["locate"].value # 해당 locate에 값을 반환
    ws.cell(row, column).value == ws["locate"].value
    ws.cell(1, 1).value # A1의 값
    ws.cell(1, 2).value # B1의 값
    ws.cell(2, 1).value # A2의 값
    # row = 1, 2, 3, 4 ...
    # column = A(1), B(2), C(3), D(4) ...
    
    ws.append(['first', 'second', 'third']) # 1줄씩 넣기
    ws.max_column # 최대 cloumn 반환
    ws.max_row # 최대 row 반환 
    ws["B"].coordinate # 셀번호를 출력
    
    ws["B"] # column B의 값 모두 가져옴
    ws["1"] # row 1의 값 모두를 한개씩 가져옴
    ws["B:C"] # column B부터 C의 값을 전부 가져옴
    ws["1:2"] # row 1부터 2의 값을 전부 가져옴
    
    ws.iter_rows(min_row=1, max_row=10, min_col=1, max_col=3) # row 1~10까지 값중 colmnun 1~3인 값만 나열  
    ws.iter_cols(min_row=1, max_row=10, min_col=1, max_col=3) # row 1~10까지 값중 colmnun 1~3인 값만 나열 
    # 이때 rows는 가로로 한줄씩 가져오고 cols는 세로로 한줄씩 가져온다.
     
    ws.insert_rows(8) # 8번째 줄 생성
    ws.insert_rows(8, 5) # 8번째 줄에 5개 줄 생성
    ws.insert_cols(2) # B번째 열 생성
    ws.insert_cols(2, 3) # B번째 열에 3개 열 생성


    
