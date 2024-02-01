import openpyxl

# 새로운 엑셀 파일 생성
wb = openpyxl.Workbook()

# 현재 활성화된 시트 선택
ws = wb.active

# 시트 이름 변경
ws.title = '자동화로만든겅미'

# 엑셀 저장
wb.save('자동화된엑셀.xlsx')