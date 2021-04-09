#import openpyxl 
import xlrd 
import xlwt 
resistor = "IC LDO REG 500mA 1.2 V, TO220-3, POS FIXED, 2.1-6V IN,1.2OUT"
location = ""
count = 0
workbook = xlrd.open_workbook('ECEparts.xls')

first_sheet = workbook.sheet_by_index(0)

descriptdata = {}
locationdata = {}

#read a row
print (first_sheet.row_values(0))


# Value of 1st row and 1st column
cell = first_sheet.cell(26, 1).value
#print (cell) 
#if sheet.cell(0, 0).value == xlrd.empty_cell.value:
    # Do something

rows = first_sheet.nrows
cols = first_sheet.ncols
#loop to parse entire sheet
for row in range(rows):
   for col in range(cols):
      cellB = first_sheet.cell(row, 1) 
      cellE = first_sheet.cell(row, 4) 
      #find a close match to the search

      if cellE.value == resistor :
         location = cellB.value
         break
      
      locationdata[cellB] = {}
      #print(cellB.value)


for row in range(rows):
   for col in range(cols):
      cellE = first_sheet.cell(row, 4) 
      descriptdata[cellE] = {}
      #print(cellE.value)
     




#print (descriptdata)
#print (locationdata)
print (location)

#print (locationdata[1:3])