#import openpyxl 
import xlrd 
import xlwt
import send as output 
import tkinter as tkinter
from tkinter import messagebox

def search(input):
   try:
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
               output.data_transmit("A11")
               return "A11"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("A12")
                  return "A12"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("A13")
                  return "A13"
      #B1x         
      if(location[0] == "B"):
         if(location[2] == "1"):
            if(location[4:6] <= "059"):
               output.data_transmit("B11")
               return "B11"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("B12")
                  return "B12"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("B13")
                  return "B13"
      #C1x
      if(location[0] == "C"):
         if(location[2] == "1"):
            if(location[4:6] <= "059"):
                  output.data_transmit("C11")
                  return "C11"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("C12")
                  return "C12"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("C13")
                  return "C13"
      #A2x
      if(location[0] == "A"):
         if(location[2] == "2"):
            if(location[4:6] <= "059"):
               output.data_transmit("A21")
               return "A21"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("A22")
                  return "A22"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("A23")
                  return "A23"
      #B2x
      if(location[0] == "B"):
         if(location[2] == "2"):
            if(location[4:6] <= "059"):
               output.data_transmit("B21")
               return "B21"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("B22")
                  return "B22"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("B23")
                  return "B23"
      #C2x
      if(location[0] == "C"):
         if(location[2] == "2"):
            if(location[4:6] <= "059"):
               output.data_transmit("C21")
               return "C21"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("C22")
                  return "C22"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("C23")
                  return "C23"

      #A3x
      if(location[0] == "A"):
         if(location[2] == "3"):
            if(location[4:6] <= "059"):
               output.data_transmit("A31")
               return "A31"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("A32")
                  return "A32"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("A33")
                  return "A33"
      #B3x
      if(location[0] == "B"):
         if(location[2] == "3"):
            if(location[4:6] <= "059"):
               output.data_transmit("B31")
               return "B31"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("B32")
                  return "B32"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("B33")
                  return "B33"
      #C3x
      if(location[0] == "C"):
         if(location[2] == "3"):
            if(location[4:6] <= "059"):
               output.data_transmit("C31")
               return "C31"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("C32")
                  return "C32"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("C33")
                  return "C33"
      #A4x
      if(location[0] == "A"):
         if(location[2] == "4"):
            if(location[4:6] <= "059"):
               output.data_transmit("A41")
               return "A41"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("A42")
                  return "A42"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("A43")
                  return "A43"
      #B4x
      if(location[0] == "B"):
         if(location[2] == "4"):
            if(location[4:6] <= "059"):
               output.data_transmit("B41")
               return "B41"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("B42")
                  return "B42"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("B43")
                  return "B43"
      #C4x
      if(location[0] == "C"):
         if(location[2] == "4"):
            if(location[4:6] <= "059"):
               output.data_transmit("C41")
               return "C41"
            if(location[4:6] >= "060"):
               if(location[4:6] <= "120"):
                  output.data_transmit("C42")
                  return "C42"
            if(location[4:6] >= "121"):
               if(location[4:6] <= "180"):
                  output.data_transmit("C43")
                  return "C43"      


      print (location)

      #print (locationdata[1:3])
   except:
      messagebox.showerror("Error", "Item not found")