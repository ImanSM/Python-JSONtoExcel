import requests
import json
import xlsxwriter

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

pass_times = response.json()['people']
astros = []

for d in pass_times:
    name = d['name']
    astros.append(name)

print(astros)
workbook = xlsxwriter.Workbook("array_values.xlsx")
worksheet = workbook.add_worksheet("Array Values")
worksheet.write("A1", "Names")

for i, value in enumerate(astros):
    worksheet.write(i+1, 0, value)

workbook.close()

