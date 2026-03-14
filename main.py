from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_model
from sqlalchemy.orm import Session

app = FastAPI()

database_model.Base.metadata.create_all(bind=engine)

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


# Dependency init and Injection
def get_db():
    db = session()
    
    try:
        yield db
    finally:
        db.close()

# Database init - only for trasfer data from List or Dictionary
def init_db():
    db = session()

    count = db.query(database_model.Product).count

    if count == 0:
        for product in products:
            db.add(database_model.Product(**product.model_dump())) # ** means unpacking- modle_dump gives row data but ** manage it for the database structure

        db.commit()
    

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)): # Under brekact - Dependency Injection
    
    db_products = db.query(database_model.Product).all()
    return db_products

# Fetch Single product
@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)): # Under brekact - Dependency Injection
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
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





