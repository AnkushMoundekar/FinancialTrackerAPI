# FinancialTrackerAPI
A production-style Expense & Income Tracking REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy** following clean architecture principles.

The application allows users to securely manage their finances by tracking expenses and income, organizing transactions into categories, and viewing financial analytics.

---

##  Features

### Authentication
- JWT Authentication
- Access Token
- Refresh Token
- Secure Password Hashing
- Login & Logout
- Refresh Token Revocation
- Protected APIs

### User Management
- User Registration
- Secure Login
- Soft Delete Support
- Active User Validation

### Expense Management
- Create Expense
- Update Expense
- Delete Expense (Soft Delete)
- List Expenses
- Pagination
- Filtering
- Sorting

### Categories
- Global Categories
- User Custom Categories
- Category Validation
- Duplicate Category Prevention

### Analytics
- Income Summary
- Expense Summary
- Balance Calculation
- Monthly Analytics
- Category-wise Spending
- Dashboard APIs

### Security
- Password Hashing using Argon2
- JWT Authentication
- HTTP Bearer Authentication
- Refresh Token Rotation
- Token Revocation
- SQL Injection Protection via ORM

### API Design
- RESTful APIs
- Request Validation using Pydantic
- Standard Response Models
- Global Exception Handling
- Dependency Injection

### Database
- PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations
- UUID Primary Keys
- Soft Delete
- Relationships
- Constraints

### Deployment
- Docker Support
- Docker Compose
- Environment Variables
- Production Ready Structure
