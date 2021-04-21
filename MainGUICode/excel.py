#This file is for communitcation with the Main GUI specific search page, It takes a string input by the user and searches the NDSU ece parts inventory display excel sheet for the location
#import openpyxl 
import xlrd 
import xlwt 
import difflib
import tkinter as tkinter
from tkinter import messagebox

#Currently working on getting difflib to find nearest match searches from the user so instead of needing an exact string the user can type in what they want.
#Future Updates could include making the get closest string functionality more efficent and effective.


#  https://docs.python.org/3/library/difflib.html#difflib.get_close_matches

#The above link is documentation on the difflib library that is being used to get closes strings on the search code.
def search(input):
   try:
      #input = "IC LDO REG 500mA 1.2 V, TO220-3, POS FIXED, 2.1-6V IN,1.2OUT" <==== test location
      location = ""
      count = 0
      workbook = xlrd.open_workbook('StorageRoomData.xls')          # <===== if the sheet name ever changes the file name needs to change here as well otherwise the code will not initalize

      first_sheet = workbook.sheet_by_index(0)

      #some useful arrays that are initalized to create dictionarys to parse if needed
      descriptdata = {}
      locationdata = {}

      #read a row
      #print (first_sheet.row_values(0))


      # Value of 1st row and 1st column
      cell = first_sheet.cell(26, 1).value
      #print (cell) 
      #if sheet.cell(0, 0).value == xlrd.empty_cell.value:
         # Do something

      rows = first_sheet.nrows
      cols = first_sheet.ncols
   
      for row in range(rows):
         for col in range(cols):
            cellE = first_sheet.cell(row, 4) 
            descriptdata[cellE] = {}
            #print(cellE.value)
          
      #this is the difflib get closest match statements. Ive taken strings from the quick search buttons to add into here to try and help the user with the searches.

      #I need to test how this looks rigt now because if these can get working all I need to do is to take the cellE.data input and before parsing for location send it 
      #through the get closest match to find an appropriate string from the sheet. Then that string can be sent as the cellE data input to look for location.
      #Testing from home is hard but these are example strings
      print(descriptdata) 
      dResistor = difflib.get_close_matches('Resistor', descriptdata, 5, 0.5)
      
      dOpamp = difflib.get_close_matches('Op amp', descriptdata, 5, 0.5)
            
      dVReg = difflib.get_close_matches('V Reg', descriptdata, 5, 0.5)
            
      dInductor = difflib.get_close_matches('Inductor', descriptdata, 5, 0.5)
            
      dDiode = difflib.get_close_matches('Diode', descriptdata, 5, 0.5)
            
      dCapacitor = difflib.get_close_matches('Capacitor', descriptdata, 5, 0.5)
            
      dZener = difflib.get_close_matches('Zener', descriptdata, 5, 0.5)
            
      dCmosLogic = difflib.get_close_matches('Cmos Logic', descriptdata, 5, 0.5)
            
      dTTLLogic = difflib.get_close_matches('TTL Logic', descriptdata, 5, 0.5)
            
      dMultiplexer = difflib.get_close_matches('Multiplexer', descriptdata, 5, 0.5)
            
      dFlipFlop = difflib.get_close_matches('Flip-Flop', descriptdata, 5, 0.5)
            
      dCrystal = difflib.get_close_matches('Crystal', descriptdata, 5, 0.5)
            
      dMicrocontrollers = difflib.get_close_matches('Microcontrollers', descriptdata, 5, 0.5)

      #not sure if dinput will work in order to test input strings
      dinput = difflib.get_close_matches(input , descriptdata, 5, 0.5)
      print("This is dinput: ")
   
      #loop to parse entire sheet
      for row in range(rows): 
         for col in range(cols):
            cellB = first_sheet.cell(row, 1) 
            cellE = first_sheet.cell(row, 4) 
            #find a close match to the search

            #This statement requires Exact string from the input to be able to search the spreadsheet
            if cellE.value == input :
               location = cellB.value
               break

            if cellE.value == dFlipFlop :
               location = cellB.value
               break

            if cellE.value == dMicrocontrollers :
               location = cellB.value
               break

            if cellE.value == dMultiplexer:
               location = cellB.value
               break

            if cellE.value == dOpamp :
               location = cellB.value
               break

            if cellE.value == dResistor :
               location = cellB.value
               break

            if cellE.value == dVReg :
               location = cellB.value
               break

            if cellE.value == dInductor :
               location = cellB.value
               break

            if cellE.value == dDiode :
               location = cellB.value
               break

            if cellE.value == dCapacitor :
               location = cellB.value
               break

            if cellE.value == dZener :
               location = cellB.value
               break

            if cellE.value == dCmosLogic :
               location = cellB.value
               break

            if cellE.value == dTTLLogic :
               location = cellB.value
               break

            if cellE.value == dCrystal :
               location = cellB.value
               break
      

            locationdata[cellB] = {}
            #print(cellB.value)
      
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
   except Exception as e:
      print(e.__class__)
      messagebox.showerror("Error", "Item not found")
      return "BAD"