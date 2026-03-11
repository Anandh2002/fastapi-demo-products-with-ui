from fastapi import FastAPI,Depends
from models import Product
from database import session,engine
import database_models
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(CORSMiddleware,allow_origins=["http://localhost:3000"],allow_methods=["*"])


database_models.Base.metadata.create_all(bind=engine)

def get_db():
    db=session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greet():
    return "Welcome"


products = [
    Product(id=1, name="Laptop", description="15 inch laptop with 16GB RAM", price=75000.0, quantity=10),
    Product(id=2, name="Smartphone", description="5G Android smartphone", price=25000.0, quantity=25),
    Product(id=3, name="Wireless Mouse", description="Bluetooth ergonomic mouse", price=1200.0, quantity=50),
    Product(id=4, name="Keyboard", description="Mechanical RGB keyboard", price=3500.0, quantity=15),
    Product(id=5, name="Monitor", description="24 inch Full HD monitor", price=12000.0, quantity=8)
]

def init_db():
    db=session()
    count=db.query(database_models.Product).count
    if count==0:      
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()

init_db()



@app.get("/products")
def get_all_products(db:Session=Depends(get_db)):
    db_products=db.query(database_models.Product).all()

    return db_products


@app.get("/products/{id}")
def get_product_by_id(id:int,db:Session=Depends(get_db)):

    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()

    if db_product:

        return db_product    
    return 'Product Not found'

@app.post("/products")
def add_product(product:Product,db:Session=Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/products/{id}")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db_product.name=product.name
        db_product.description=product.description
        db_product.price=product.price
        db_product.quantity=product.quantity
        db.commit()

        return "Product updated successfully"
        
    return "Product not found"

@app.delete("/products/{id}")
def delete_product(id:int,db:Session=Depends(get_db)):
    db_product=db.query(database_models.Product).filter(database_models.Product.id==id).first()
    if db_product:
        db.delete(db_product)
        db.commit()

        return "product deleted successfully"
        
    return "Product not found"
    



