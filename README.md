# Ecommerce FastAPI Backend

A FastAPI-based ecommerce backend application with MongoDB integration, featuring product and order management APIs.

## Features

- **Products API**: Create and list products with filtering and pagination
- **Orders API**: Create orders and retrieve user orders
- **MongoDB Integration**: Uses MongoDB for data persistence
- **Pagination**: Efficient pagination for large datasets
- **Filtering**: Support for product filtering by name and size
- **Data Validation**: Pydantic models for request/response validation

## API Endpoints

### Products

- `POST /products` - Create a new product
- `GET /products` - List products with optional filtering

### Orders

- `POST /orders` - Create a new order
- `GET /orders/{user_id}` - Get orders for a specific user

## Setup Instructions

### Prerequisites

- Python 3.10+ 
- MongoDB (local or MongoDB Atlas)

### Local Development

1. **Clone the repository**
   \`\`\`bash
   git clone <repository-url>
   cd ecommerce-fastapi
   \`\`\`

2. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Configure MongoDB**
   
   **Option A: MongoDB Atlas (Recommended)**
   - Create a free MongoDB Atlas account
   - Create a new cluster (M0 free tier)
   - Get your connection string
   - Set environment variables:
     \`\`\`bash
     export MONGODB_USERNAME=your_username
     export MONGODB_PASSWORD=your_password
     export MONGODB_CLUSTER=cluster0.xxxxx.mongodb.net
     \`\`\`

   **Option B: Local MongoDB**
   - Install MongoDB locally
   - Update `database.py` to use local connection string

4. **Create database indexes**
   \`\`\`bash
   python database.py
   \`\`\`

5. **Seed the database (optional)**
   \`\`\`bash
   python scripts/seed_data.py
   \`\`\`

6. **Run the application**
   \`\`\`bash
   uvicorn main:app --reload
   \`\`\`

   The API will be available at `http://localhost:8000`

### Docker Deployment

1. **Build the Docker image**
   \`\`\`bash
   docker build -t ecommerce-api .
   \`\`\`

2. **Run the container**
   \`\`\`bash
   docker run -p 8000:8000 \
     -e MONGODB_USERNAME=your_username \
     -e MONGODB_PASSWORD=your_password \
     -e MONGODB_CLUSTER=cluster0.xxxxx.mongodb.net \
     ecommerce-api
   \`\`\`

### Deployment to Render/Railway

1. **Render Deployment**
   - Connect your GitHub repository to Render
   - Set environment variables in Render dashboard
   - Deploy as a Web Service

2. **Railway Deployment**
   - Connect your GitHub repository to Railway
   - Set environment variables in Railway dashboard
   - Deploy the service

## API Documentation

Once the application is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Database Schema

### Products Collection
\`\`\`json
{
  "_id": "ObjectId",
  "name": "string",
  "price": "number",
  "sizes": [
    {
      "size": "string",
      "quantity": "number"
    }
  ]
}
\`\`\`

### Orders Collection
\`\`\`json
{
  "_id": "ObjectId",
  "userId": "string",
  "items": [
    {
      "productId": "string",
      "qty": "number"
    }
  ],
  "created_at": "datetime"
}
\`\`\`

## Environment Variables

- `MONGODB_USERNAME`: MongoDB username
- `MONGODB_PASSWORD`: MongoDB password  
- `MONGODB_CLUSTER`: MongoDB cluster URL

## Testing

You can test the APIs using the provided Swagger UI or with curl commands:

\`\`\`bash
# Create a product
curl -X POST "http://localhost:8000/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Product",
    "price": 99.99,
    "sizes": [{"size": "large", "quantity": 10}]
  }'

# List products
curl "http://localhost:8000/products?limit=10&offset=0"

# Create an order
curl -X POST "http://localhost:8000/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "userId": "user123",
    "items": [{"productId": "PRODUCT_ID", "qty": 2}]
  }'

# Get user orders
curl "http://localhost:8000/orders/user123?limit=10&offset=0"
\`\`\`

## Performance Considerations

- Database indexes are created for frequently queried fields
- Pagination is implemented to handle large datasets efficiently
- Connection pooling is handled by PyMongo automatically
- Proper error handling and validation throughout the application

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request
