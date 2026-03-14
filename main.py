from fastapi import FastAPI
from models import Product
from database import session

app = FastAPI()

@app.get("/")

def greet():
    return "Welcome to my server!"


# product = [
#     Product(1, "Phone", "Budget Phone", 99, 10),
#     Product(2, "Laptop", "Gaiming laptop", 999, 6)
# ]

products = [
    Product(id=1, name="Phone", description="A smartphone", price=99.98, quantity=50),
    Product(id=2, name="Laptop", description="Gaiming laptop", price=699.98, quantity=10),
    Product(id=3, name="Pen", description="A blue ink pen", price=10.98, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=196.10, quantity=5)
]

@app.get("/products")
def get_all_products():
    # db connection
    db = session()
    return products

# Fetch Single product
@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Product Not found"

# Add product
@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


# Update Product

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully"
    
    return "Product not found!"

# Product Delete
@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted Successfully!"
    return "Product not found!"





