#Reading file
fd = open('Inventory.txt','r')  
products = fd.read().split('\n')
fd.close()

#customer details - user input
ui_username = input("Enter your Name: ")
ui_phone    = input("Enter your Phone No: ")
ui_mail     = input("Enter your Mail: ")
ui_prod_id  = input("Enter product ID: ")
ui_prod_qn  = input("Enter product Quantity: ")

#Product avaliability 
updated_product_lst = []

for product in products:
    
    prod_details = product.split(',')

    if(prod_details[0] == ui_prod_id):
        
        if (int(ui_prod_qn) <= int(prod_details[3])):  
            print("-----------------------------")
            print("Product Name     : ", prod_details[1])
            print("Price            : ", prod_details[2]) 
            print("Quantity         : ", ui_prod_qn) 
            print("-----------------------------")
            print("Billing Amount   : ", int(ui_prod_qn) * int(prod_details[2]))
            print("-----------------------------")

            prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))
            
            fd = open("Sales.txt",'a')
            sales_detail = ui_username +","+ ui_phone +","+ ui_mail +","+ prod_details[1] +","+ ui_prod_id +","+ ui_prod_qn +","+ str(int(ui_prod_qn) * int(prod_details[2]))+","+ time.ctime()+ "\n"
            fd.write(sales_detail)
            fd.close()


#handling insufficient data
else:
            print("Sorry, We're not having enough quantity.")
            print("We're having only", prod_details[3], 'quantity.')
            print("Would you like to purchase it?")
            
            ch = input("Press Y/N: ")
            
            if (ch == 'Y' or ch == 'y'):  # If customer agrees to buy available stock
                print("-----------------------------")
                print("Product Name     : ", prod_details[1])
                print("Price            : ", prod_details[2]) 
                print("Quantity         : ", prod_details[3]) 
                print("-----------------------------")
                print("Billing Amount   : ", int(prod_details[3]) * int(prod_details[2]))
                print("-----------------------------")

                # Updating Inventory list
                prod_details[3] = '0'  # Marking product as out of stock

# update inventory
updated_product_lst.append(prod_details)

lst = []

for i in updated_product_lst:
    prod = i[0] +","+  i[1] +","+ i[2] +","+ i[3] + '\n'
    lst.append(prod)

lst[-1] = lst[-1][:-1]  # Remove last newline character

# Writing Updated Inventory to File
fd = open('Inventory.txt','w')

for i in lst:
    fd.write(i)

fd.close()

print("-------------------")
print("Inventory Updated")
