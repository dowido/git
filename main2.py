from database import Product
try:
    p_name=(input("enter product name"))
    p_qty=int(input("enter qty"))
    p_price=input("enter price")
    Product.create(name =p_name, qty =p_qty, price =p_price)
    print ("saved successfully")
except:
    print("Error")