import pandas as pd
import xlsxwriter
import webScrapingSample

data = pd.read_csv("python.csv", low_memory=False)
print("total number{0}" .format(len(data)))
print(list(data))
book = xlsxwriter.Workbook("example2.xlsx")
sheet = book.add_worksheet()
row=0
column=0
'''
for item in data:
    sheet.write(row, column,item)
    column += 1
    '''
for item in webScrapingSample.soup.select('.homecontent'):
    sheet.write(row, column, item.text)
    row += 1

book.close()
