from openpyxl import load_workbook

wb = load_workbook(filename="res/final_pst.xlsx") # add your own file can't upload file to github

current_sheet = wb['Sheet1']
print(current_sheet.max_row)
# Column 3 = Name
# Column 4 = FName
# Column 5 = DOB
# Column 6 = NICf

for x in range(1, 11):
  name = current_sheet.cell(row=x, column=3).value
  f_name = current_sheet.cell(row=x, column=4).value
  dob = current_sheet.cell(row=x, column=5).value
  nic = current_sheet.cell(row=x, column=6).value
  print(f'Name = {name}, Father Name = {f_name}, Date Of Birth = {dob}, NIC = {nic}, ')