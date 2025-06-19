#Read file
fd = open('Inventory.txt', 'r')

# Read and split the inventory into products
products = fd.read().split('\n')

fd.close()

#Process the purchase
ui_prod_id = input("Enter product ID: ")
ui_prod_qn = input("Enter product Quantity: ")

updated_product_lst = []  # To store updated inventory

#Save and update inventory
for product in products:
    prod_details = product.split(',') 
    
    if prod_details[0] == ui_prod_id:  
        print("-----------------------------")
        print("Product Name     : ", prod_details[1])
        print("Price            : ", prod_details[2]) 
        print("Quantity         : ", ui_prod_qn) 
        print("-----------------------------")
        
        # Calculate Billing Amount
        billing_amount = int(ui_prod_qn) * int(prod_details[2])
        print("Billing Amount   : ", billing_amount)
        print("-----------------------------")
        
        # Main Deduct the purchased quantity from inventory (UPDATION)
        prod_details[3] = str(int(prod_details[3]) - int(ui_prod_qn))
    
    updated_product_lst.append(prod_details)
