# Question: Inventory Management Application
# Example Run:
# INVENTORY MANAGEMENT
# ==============================
# 1. Add Product
# 2. View Products
# 3. Search Product
# 4. Inventory Value
# 5. Delete Product
# 6. Exit

product_list = []
def add_product():
    p_id=int(input("Enter Product Id:"))
    p_name=input("Enter Product Name:")
    p_price=int(input("Enter Price:"))
    p_quantity=int(input("Enter Quantity:"))
    p_data={
        "p_id": p_id,
        "p_name": p_name,
        "p_price": p_price,
        "p_quantity":p_quantity
    }
    product_list.append(p_data)
    print("Product Successfully Added")
def view_product():
    for product in product_list:
        print(product)

def search_product():
    product_id= input("Enter Product Id: ")
    for product in product_list:
        if product['p_id']==product_id:
            print(product)
        else:
            print("Product Not Found")

def total_inventory():
    total=0
    count=0
    for product in product_list:
        total += product["total_price"]
        count += 1
        print("Total inventory:{total},Total Count:{count}")
        
