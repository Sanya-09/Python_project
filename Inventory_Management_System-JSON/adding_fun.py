import json

fd = open('Record.json', 'r')
js = fd.read()
fd.close()

record = json.loads(js)

print("--------------------MENU---------------------")
for key in record.keys():
    print(key, record[key]['Name'], record[key]['Price'], record[key]['Qn'])
print("---------------------------------------------")
print('')

ui_pr = str(input("Enter product ID : "))
ui_qn = int(input("Enter Quantity   : "))

if (record[ui_pr]['Qn'] >= ui_qn):
    print("Name      : ", record[ui_pr]["Name"])
    print("Price (Rs): ", record[ui_pr]["Price"])
    print("Quantity  : ", ui_qn)
    print("---------------------------------------------")
    print("Billing   : ", ui_qn * record[ui_pr]["Price"], "Rs")
    print("---------------------------------------------")

    # Reduce the stock
    record[ui_pr]['Qn'] = record[ui_pr]['Qn'] - ui_qn
    
else:
    print("Sorry, We're not having enough quantity of product in our Inventory.")
    print("We're only having " + str(record[ui_pr]['Qn']) + " quantity.")
    print("---------------------------------------------")

else:
    
    print("Sorry, We're not having enough quanity of product in our Inventory.")
    print("We're only having " + str(record[ui_pr]['Qn']) + " quantity.")
    print("---------------------------------------------")
    
    ch == str(raw_input("Press Y to purchase: "))
    
    if(ch == "Y" or ch == 'y'):

        print("---------------------------------------------")
        print("Name      : ", record[ui_pr]["Name"])
        print("Price (Rs): ", record[ui_pr]["Price"])
        print("Quantity  : ", record[ui_pr]['Qn'])
        print("---------------------------------------------")
        print("Billing   : ", record[ui_pr]['Qn'] * record[ui_pr]["Price"], "Rs")
        print("---------------------------------------------")

        record[ui_pr]['Qn'] = 0
        
    else:
        print("Thanks!")

  js = json.dumps(record)

fd = open('Record.json', 'w')
fd.write(js)
fd.close()
