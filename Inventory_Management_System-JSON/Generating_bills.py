# Inventory stored as a dictionary
record = {
    1001: {'Name': "5 Star", "Price": 10, "Qn": 200},
    1002: {'Name': "Bar-One", "Price": 20, "Qn": 100},
    1003: {'Name': "Candy", "Price": 2, "Qn": 1000},
    1004: {'Name': "Chocolate Cake", "Price": 550, "Qn": 8},
    1005: {'Name': "Blueberry Cake", "Price": 650, "Qn": 5}
}

# Displaying the menu
print("--------------------MENU---------------------")
for key in record.keys():# Printing Bill
print("Name      : ", record[ui_pr]["Name"])
print("Price (Rs): ", record[ui_pr]["Price"])
print("Quantity  : ", ui_qn)
print("---------------------------------------------")
print("Billing   : ", ui_qn * record[ui_pr]["Price"], "Rs")
print("---------------------------------------------")
    print(key, record[key]['Name'], record[key]['Price'], record[key]['Name'])
print("---------------------------------------------")
print('')

# Taking input from user
ui_pr = int(input("Enter product ID : "))
ui_qn = int(input("Enter Quantity   : "))

