# adding boundary conditions, if user need is more then the available quantity

# Going through each product detail
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

            # Update stock quantity
            prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))
            
        else:
            # If stock is insufficient, inform the user
            
            print("Sorry, We're not having enough quantity.")
            print("We're having only", prod_details[3], 'quantity.')
            print("Would you like to purchase it?")
            
            ch = input("Press Y/N: ")
            
            if (ch == 'Y' or ch == 'y'):
                # If user agrees to purchase available stock
                
                print("-----------------------------")
                print("Product Name     : ", prod_details[1])
                print("Price            : ", prod_details[2]) 
                print("Quantity         : ", prod_details[3]) 
                print("-----------------------------")
                print("Billing Amount   : ", int(prod_details[3]) * int(prod_details[2]))
                print("-----------------------------")

                # Update inventory by selling all available stock
                prod_details[3] = '0'
            else:
                print("Thanks")
            
    # Add product details to the updated list
    updated_product_lst.append(prod_details)

#Updating inventory
lst = []

for i in updated_product_lst:
    prod = i[0] +","+  i[1] +","+ i[2] +","+ i[3] + '\n'
    lst.append(prod)

lst[-1] = lst[-1][:-1]  # Remove the last newline character


fd = open('Inventory.txt','w')

for i in lst:
    fd.write(i)

fd.close()

print("-------------------")
print("Inventory Updated")
