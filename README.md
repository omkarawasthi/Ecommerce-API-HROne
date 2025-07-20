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
   cd ecommerce-API-HROne
   \`\`\`

2. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Run the application**
   \`\`\`bash
   uvicorn main:app --reload
   \`\`\`

   The API will be available at `http://localhost:8000`




