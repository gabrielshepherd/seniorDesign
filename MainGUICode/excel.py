#import openpyxl 
import xlrd 
import xlwt
import send as output 

def search(input):
   #input = "IC LDO REG 500mA 1.2 V, TO220-3, POS FIXED, 2.1-6V IN,1.2OUT"
   location = ""
   count = 0
   workbook = xlrd.open_workbook('StorageRoomData.xls')

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

         if cellE.value == input :
            location = cellB.value
            break
   
         locationdata[cellB] = {}
         #print(cellB.value)

   for row in range(rows):
      for col in range(cols):
         cellE = first_sheet.cell(row, 4) 
         descriptdata[cellE] = {}
         #print(cellE.value)
      

   #0-59 is 1 60-120 is 2 121-180 is 3

   #A1x
   if(location[0] == "A"):
      if(location[2] == "1"):
         if(location[4:6] <= "059"):
            #output.data_transmit("A11")
            print("Transmitted Data")
         if(location[4:6] >= "060"):
            if(location[4:6] <= "120"):
            #output.data_transmit("A12")
               print("Transmitted Data")
         if(location[4:6] >= "121"):
            if(location[4:6] <= "180"):
            #output.data_transmit("A13")
               print("Transmitted Data")
   #B1x         
   if(location[0] == "B"):
      if(location[2] == "1"):
         if(location[4:6] <= "059"):
            #output.data_transmit("B11")
               print("Transmitted Data")
         if(location[4:6] >= "060"):
            if(location[4:6] <= "120"):
            #output.data_transmit("B12")
               print("Transmitted Data")
         if(location[4:6] >= "121"):
            if(location[4:6] <= "180"):
            #output.data_transmit("B13")
               print("Transmitted Data")
   #C1x
   if(location[0] == "C"):
      if(location[2] == "1"):
         if(location[4:6] <= "059"):
            #output.data_transmit("C11")
               print("Transmitted Data")
         if(location[4:6] >= "060"):
            if(location[4:6] <= "120"):
            #output.data_transmit("C12")
               print("Transmitted Data")
         if(location[4:6] >= "121"):
            if(location[4:6] <= "180"):
            #output.data_transmit("C13")
               print("Transmitted Data")
   #A2x
   if(location[0] == "A"):
      if(location[2] == "2"):
         if(location[4:6] <= "059"):
            #output.data_transmit("A21")
            print("Transmitted Data")
         if(location[4:6] >= "060"):
            if(location[4:6] <= "120"):
            #output.data_transmit("A22")
               print("Transmitted Data")
         if(location[4:6] >= "121"):
            if(location[4:6] <= "180"):
            #output.data_transmit("A23")
               print("Transmitted Data")
   #B2x
   if(location[0] == "B"):
      if(location[2] == "2"):
         if(location[4:6] <= "059"):
            #output.data_transmit("B21")
            print("Transmitted Data")
         if(location[4:6] >= "060"):
            if(location[4:6] <= "120"):
            #output.data_transmit("B22")
               print("Transmitted Data")
         if(location[4:6] >= "121"):
            if(location[4:6] <= "180"):
            #output.data_transmit("B23")
               print("Transmitted Data")
   #C2x
   if(location[0] == "C"):
      if(location[2] == "2"):
         if(location[4:6] <= "059"):
            output.data_transmit("C21")
            print("Transmitted Data - C21")
         if(location[4:6] >= "060"):
            if(location[4:6] <= "120"):
            #output.data_transmit("C22")
               print("Transmitted Data")
         if(location[4:6] >= "121"):
            if(location[4:6] <= "180"):
            #output.data_transmit("C23")
               print("Transmitted Data")

   #A3x
   #C3x
   #B4x          


   if(location[0]) == "C":
   #print (descriptdata)
   #print (locationdata)
      print("")
   print (location)

   #print (locationdata[1:3])