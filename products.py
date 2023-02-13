from database import Product
users = Product.select()

for product in users:
    print(product.name, product.qty, product.price)

