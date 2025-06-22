import json
fd = open('Record.json', 'r')
js = fd.read()
fd.close()

record = json.loads(js)  # Convert JSON string to dictionary
print("--------------------MENU---------------------")
for key in record.keys():
    print(key, record[key]['Name'], record[key]['Price'], record[key]['Qn'])
print("---------------------------------------------")
print('')

# Taking user input for purchase
ui_pr = int(input("Enter product ID : "))
ui_qn = int(input("Enter Quantity   : "))

print("---------------------------------------------")
print('')

print("Name      : ", record[str(ui_pr)]["Name"])
print("Price (Rs): ", record[str(ui_pr)]["Price"])
print("Quantity  : ", ui_qn)
print("---------------------------------------------")
print("Billing   : ", ui_qn * record[str(ui_pr)]["Price"], "Rs")
print("---------------------------------------------")

# Update inventory after purchase
record[str(ui_pr)]['Qn'] = record[str(ui_pr)]['Qn'] - ui_qn
