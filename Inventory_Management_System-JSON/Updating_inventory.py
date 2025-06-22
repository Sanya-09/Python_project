record = {
    1001: {'Name': "5 Star", "Price": 10, "Qn": 200},
    1002: {'Name': "Bar-One", "Price": 20, "Qn": 100},
    1003: {'Name': "Candy", "Price": 2, "Qn": 1000},
    1004: {'Name': "Chocolate Cake", "Price": 550, "Qn": 8},
    1005: {'Name': "Blueberry Cake", "Price": 650, "Qn": 5}
}


print("--------------------MENU---------------------")
for key in record.keys():
    print(key, record[key]['Name'], record[key]['Price'], record[key]['Name'])
print("---------------------------------------------")
print('')


ui_pr = int(input("Enter product ID : "))
ui_qn = int(input("Enter Quantity   : "))

print("---------------------------------------------")
print('')


print("Name      : ", record[ui_pr]["Name"])
print("Price (Rs): ", record[ui_pr]["Price"])
print("Quantity  : ", ui_qn)
print("---------------------------------------------")
print("Billing   : ", ui_qn * record[ui_pr]["Price"], "Rs")
print("---------------------------------------------")

record[ui_pr]['Qn'] = record[ui_pr]['Qn'] - ui_qn

print('')
print("---------------------------------------------")
print("  Thanks for your order, Inventory Updated!  ")
print("---------------------------------------------")

import json

# Convert dictionary to JSON string
json_data = json.dumps(record)

# Writing to file
fd = open("records.json", "w")
fd.write(json_data)
fd.close()

print("Inventory Saved Successfully!")
