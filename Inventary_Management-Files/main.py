#Creating inventory file
with open("inventory.txt", "w") as file:
    # Write product details in a comma-separated format
    file.write("1, Chocolate, 5, 100\n")
    file.write("2, Milky Bar, 10, 50\n")
    file.write("3, Cake, 300, 5\n")
    file.write("4, Candy, 1, 200\n")

# Open the inventory file and read data
fd = open('inventory.txt', 'r')

products = fd.read().split('\n')

fd.close()

# Display each product
for product in products:
    print(product)

#Accessing Product Information
for product in products:
    details = product.split(",")
    product_id = details[0]  # Product ID
    product_name = details[1]  # Product Name
    product_price = details[2]  # Product Price
    product_quantity = details[3]  # Product Quantity

    print(f"Product ID: {product_id}, Name: {product_name}, Price: {product_price}, Quantity: {product_quantity}")

#Search for Product
ui_prod_id = input("Enter product ID: ")

for product in products:
    prod_details = product.split(',')  # Split product details

    if prod_details[0] == ui_prod_id:  # Check if ID matches
        print("-----------------------------")
        print("Product Name     : ", prod_details[1])
        print("Price            : ", prod_details[2]) 
        print("Available Stock  : ", prod_details[3])
        print("-----------------------------")
