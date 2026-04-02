💰 Finance Tracker API

A scalable backend system built using FastAPI for managing financial transactions, providing analytics, and implementing secure role-based access control using JWT authentication.

🚀 Overview

The Finance Tracker API is designed to help users manage their financial records efficiently. It supports transaction management, advanced filtering, and analytical insights such as income summaries and category breakdowns.

This project demonstrates strong backend engineering principles including modular architecture, data validation, authentication, and clean API design.

✨ Features

🔐 Authentication & Authorization

JWT-based authentication using python-jose

Role-based access control:

Admin → Full access (CRUD + analytics)

Analyst → Read + analytics

Viewer → Read-only

💰 Transaction Management

Create, Read, Update, Delete (CRUD) operations

Fields:

Amount

Type (Income / Expense)

Category

Date

Notes

🔍 Filtering & Pagination

Filter transactions by:

Type (income / expense)

Category

Pagination support:

skip and limit

📊 Analytics Engine

Total Income & Expenses

Balance Calculation

Category-wise breakdown

Monthly summaries using aggregation queries

⚠️ Validation & Error Handling

Input validation using Pydantic

Proper HTTP status codes

Clear error messages

🛠️ Tech Stack

Technology	Purpose

FastAPI	Backend framework

Python	Core language

SQLAlchemy	ORM for database

SQLite	Database

Pydantic	Data validation

JWT (python-jose)	Authentication

📁 Project Structure

finance-tracker/
│
├── app/

│   ├── main.py 
# Entry point
│   ├── database.py          # DB connection
│   ├── models.py            # ORM models
│   ├── schemas.py           # Request/response validation
│   ├── crud.py              # Business logic
│   ├── auth.py              # JWT logic
│   ├── dependencies.py      # Auth + permissions
│   ├── routes/
│   │   ├── transactions.py  # Transaction APIs
│   │   ├── analytics.py     # Analytics APIs
│   │   ├── users.py         # Auth APIs
│
├── requirements.txt
├── README.md


⚙️ Installation & Setup

1️⃣ Clone Repository

git clone https://github.com/your-username/finance-tracker.git

cd finance-tracker

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Application

uvicorn app.main:app --reload

4️⃣ Open API Docs

http://127.0.0.1:8000/docs

🔐 Authentication Flow

Call /login endpoint

Provide username and role:

{

  "username": "usha",
  
  "role": "admin"
  
}

Copy the access_token

Click Authorize 🔒 in Swagger UI

Enter:

Bearer <your_token>

📌 API Endpoints

🔑 Authentication

POST /login → Generate JWT token

💰 Transactions

POST /transactions → Create transaction

GET /transactions → Get all transactions

PUT /transactions/{id} → Update transaction

DELETE /transactions/{id} → Delete transaction

GET /transactions/filter → Filter transactions

GET /transactions/paginated → Paginated results

📊 Analytics

GET /analytics/summary → Income, Expense, Balance

GET /analytics/category → Category-wise totals

GET /analytics/monthly → Monthly summaries

🧠 Architecture & Design

Modular structure separating:

Routes

Business logic (CRUD)

Models

Validation (schemas)

Role-based access control using permission mapping

JWT-based stateless authentication

SQL aggregation for analytics queries

Clean and maintainable code organization

⚡ Example Request

Create Transaction
{

  "amount": 5000,
  
  "type": "income",
  
  "category": "salary",
  
  "date": "2026-04-02",
  
  "notes": "monthly salary"
  
}

⚠️ Error Handling

400 → Bad request / validation error

401 → Unauthorized (invalid token)

403 → Forbidden (insufficient permissions)

404 → Resource not found

🚀 Future Enhancements

User authentication with password hashing

PostgreSQL integration

Frontend dashboard (React)

Deployment on cloud (Render / AWS)

Unit testing (pytest)

🏆 Key Highlights

Built a production-style backend system

Implemented secure authentication & authorization

Designed scalable and modular architecture

Developed analytics using real database queries

👨‍💻 Author

Usha Rani
