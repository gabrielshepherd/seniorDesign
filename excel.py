#import openpyxl 
import xlrd 
import xlwt 
count = 0
workbook = xlrd.open_workbook('ECEparts.xls')

first_sheet = workbook.sheet_by_index(0)

descriptdata = {}
locationdata = {}

#read a row
print (first_sheet.row_values(0))


# Value of 1st row and 1st column
cell = first_sheet.cell(26, 1).value
print (cell) 
#if sheet.cell(0, 0).value == xlrd.empty_cell.value:
    # Do something

rows = first_sheet.nrows
cols = first_sheet.ncols
#loop to parse entire sheet
for row in range(rows):
   for col in range(cols):
      cellA = first_sheet.cell(row, 1) 
      locationdata[cellA] = {}
      print(cellA.value)


for row in range(rows):
   for col in range(cols):
      cellD = first_sheet.cell(row, 4) 
      descriptdata[cellD] = {}
      print(cellD.value)


#data[500]
