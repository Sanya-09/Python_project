ui_name = str(input("Enter your name    : "))
ui_mail = str(input("Enter Mail ID      : "))
ui_ph   = str(input("Enter Phone No     : "))
ui_pr   = str(input("Enter product ID   : "))
ui_qn   = int(input("Enter Quantity     : "))

if (record[ui_pr]['Qn'] >= ui_qn):

    print("Billing   : ", ui_qn * record[ui_pr]["Price"], "Rs")

    record[ui_pr]['Qn'] -= ui_qn

    # Prepare sales record
    sale = ui_name+","+ui_mail+","+ui_ph+","+ui_pr+","+record[ui_pr]["Name"]+","+str(ui_qn)+","+str(record[ui_pr]["Price"])+","+str(ui_qn * record[ui_pr]["Price"])+","+time.ctime()+"\n"

else:
    print("Sorry, insufficient stock.")
    print("Available quantity: " + str(record[ui_pr]['Qn']))
    
    ch = str(input("Press Y to purchase available stock: "))

    if(ch == "Y" or ch == 'y'):
        sale = ui_name+","+ui_mail+","+ui_ph+","+ui_pr+","+record[ui_pr]["Name"]+","+str(record[ui_pr]['Qn'])+","+str(record[ui_pr]["Price"])+","+str(record[ui_pr]['Qn'] * record[ui_pr]["Price"])+","+time.ctime()+"\n"
        record[ui_pr]['Qn'] = 0
    else:
        print("Thanks!")
        sale = ""  # No sale recorded

js = json.dumps(record)
# Save updated inventory
fd = open('Record.json', 'w')
fd.write(json.dumps(record))
fd.close()


fd = open('Sales.txt', 'a')
fd.write(sale)
fd.close()
