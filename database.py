from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_database():
    """Get MongoDB database connection"""
    username = os.getenv("MONGODB_USERNAME")
    password = os.getenv("MONGODB_PASSWORD" )
    cluster_url = os.getenv("MONGODB_CLUSTER")
    
    # For MongoDB Atlas
    connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/ecommerce?retryWrites=true&w=majority"
    
    try:
        client = MongoClient(connection_string)
        
        # Test the connection
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        
        # Return the database
        return client.ecommerce
        
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        # Fallback to local MongoDB for development
        try:
            client = MongoClient("mongodb://localhost:27017/")
            client.admin.command('ping')
            print("Connected to local MongoDB")
            return client.ecommerce
        except Exception as local_e:
            print(f"Error connecting to local MongoDB: {local_e}")
            raise Exception("Could not connect to any MongoDB instance")

# Create indexes for better performance
def create_indexes():
    """Create database indexes for better query performance"""
    db = get_database()
    
    # Create indexes for products collection
    db.products.create_index("name")
    db.products.create_index("sizes.size")
    
    # Create indexes for orders collection
    db.orders.create_index("userId")
    db.orders.create_index("created_at")
    
    print("Database indexes created successfully!")

if __name__ == "__main__":
    create_indexes()
