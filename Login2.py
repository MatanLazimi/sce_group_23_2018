import datetime, xlrd, xlsxwriter

Workbook = xlrd.open_workbook('Workers.xlsx')
sheet = Workbook.sheet_by_index(0)

# For row 0 and column 0
A1=sheet.cell_value(1, 4)

for i in range(sheet.ncols):
    if i==4:
        a1_datetime = datetime.datetime(*xlrd.xldate_as_tuple(A1, Workbook.datemode))
        print('datetime: %s' % a1_datetime)
    else:
        print(sheet.cell_value(1, i))





