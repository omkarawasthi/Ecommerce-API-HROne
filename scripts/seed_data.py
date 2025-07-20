"""
Script to seed the database with sample data for testing
"""
from database import get_database
from datetime import datetime

def seed_database():
    """Seed the database with sample products and orders"""
    db = get_database()
    
    # Clear existing data (optional - remove in production)
    print("Clearing existing data...")
    db.products.delete_many({})
    db.orders.delete_many({})
    
    # Sample products
    sample_products = [
        {
            "name": "T-Shirt",
            "price": 25.99,
            "sizes": [
                {"size": "small", "quantity": 10},
                {"size": "medium", "quantity": 15},
                {"size": "large", "quantity": 8}
            ]
        },
        {
            "name": "Jeans",
            "price": 79.99,
            "sizes": [
                {"size": "small", "quantity": 5},
                {"size": "medium", "quantity": 12},
                {"size": "large", "quantity": 7},
                {"size": "xl", "quantity": 3}
            ]
        },
        {
            "name": "Sneakers",
            "price": 129.99,
            "sizes": [
                {"size": "8", "quantity": 4},
                {"size": "9", "quantity": 6},
                {"size": "10", "quantity": 8},
                {"size": "11", "quantity": 5}
            ]
        },
        {
            "name": "Hoodie",
            "price": 59.99,
            "sizes": [
                {"size": "small", "quantity": 8},
                {"size": "medium", "quantity": 10},
                {"size": "large", "quantity": 12},
                {"size": "xl", "quantity": 6}
            ]
        },
        {
            "name": "Baseball Cap",
            "price": 19.99,
            "sizes": [
                {"size": "one-size", "quantity": 20}
            ]
        }
    ]
    
    # Insert products
    print("Inserting sample products...")
    result = db.products.insert_many(sample_products)
    product_ids = [str(id) for id in result.inserted_ids]
    print(f"Inserted {len(product_ids)} products")
    
    # Sample orders
    sample_orders = [
        {
            "userId": "user_1",
            "items": [
                {"productId": product_ids[0], "qty": 2},
                {"productId": product_ids[1], "qty": 1}
            ],
            "created_at": datetime.utcnow()
        },
        {
            "userId": "user_2",
            "items": [
                {"productId": product_ids[2], "qty": 1}
            ],
            "created_at": datetime.utcnow()
        },
        {
            "userId": "user_1",
            "items": [
                {"productId": product_ids[3], "qty": 1},
                {"productId": product_ids[4], "qty": 2}
            ],
            "created_at": datetime.utcnow()
        }
    ]
    
    # Insert orders
    print("Inserting sample orders...")
    result = db.orders.insert_many(sample_orders)
    print(f"Inserted {len(result.inserted_ids)} orders")
    
    print("Database seeded successfully!")
    
    # Print some stats
    product_count = db.products.count_documents({})
    order_count = db.orders.count_documents({})
    print(f"Total products: {product_count}")
    print(f"Total orders: {order_count}")

if __name__ == "__main__":
    seed_database()
