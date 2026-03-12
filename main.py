from fastapi import FastAPI
from models import Product

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


