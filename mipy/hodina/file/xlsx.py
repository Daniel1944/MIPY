import xlrd
import matplotlib.pyplot as plt
import numpy as np

wb = xlrd.open_workbook("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\topeni.xlsx")
sheet = wb.sheet_by_index(0)

print(sheet.cell(5, 5))

wb = xlrd.open_workbook("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\topeni.xlsx")
sheet = wb.sheet_by_index(0)

for i in range(2, sheet.nrows - 1):
    for j in range(2, sheet.ncols - 1, 4):
        #print("{:10.3f} ".format(sheet.cell_value(i, j)))
        print(sheet.cell_value(i,j))

plt.show()
