
from models import Product

def seed_products(db):
    mock_items = [
        {"name": "Classic White Shirt", "price": 999.99, "description": "Cotton shirt for men", "image_url": "https://example.com/shirt1.jpg"},
        {"name": "Blue Denim Jeans", "price": 1499.99, "description": "Stylish denim for women", "image_url": "https://example.com/jeans.jpg"},
    ]
    for item in mock_items:
        db.session.add(Product(**item))
    db.session.commit()
