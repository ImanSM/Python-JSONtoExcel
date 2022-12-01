import requests
import json
import xlsxwriter

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

# This saves JSON data into an array
pass_times = response.json()['people']
astros = []

for d in pass_times:
    name = d['name']
    astros.append(name)

# This writes the excel file
print(astros)
workbook = xlsxwriter.Workbook("arraysample.xlsx")
worksheet = workbook.add_worksheet("Array Values")
worksheet.write("A1", "Names")

for i, value in enumerate(astros):
    worksheet.write(i+1, 0, value)

workbook.close()

