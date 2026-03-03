# DRF E-Commerce Backend

Backend-only e-commerce API built with Django Rest Framework using clean app boundaries.

## Apps
- `users/` - custom user model, role permissions, auth and admin user management
- `products/` - product model, search/filter/pagination and product ownership permissions
- `orders/` - order creation, stock deduction and order history data
- `vendors/` - vendor-focused product CRUD APIs
- `customers/` - customer-focused order history APIs

## Key Features
- Custom `User` model extending `AbstractUser`
- Roles: `ADMIN`, `CUSTOMER`, `VENDOR`
- JWT auth (`/api/auth/token/` and `/api/auth/token/refresh/`)
- Separate registration endpoints for customer/vendor
- Duplicate prevention:
  - username/email unique (users)
  - `(name, vendor)` unique constraint (products)
- Product listing with pagination, filter, search, ordering
- Order total auto-calculation and immutable purchase timestamp
- Admin-only user management and order update/delete

## API Overview
- `POST /api/auth/register/customer/`
- `POST /api/auth/register/vendor/`
- `POST /api/auth/token/`
- `POST /api/auth/token/refresh/`
- `GET /api/products/` (customer/vendor/admin)
- `GET /api/products/{id}/`
- `POST/PUT/PATCH/DELETE /api/products/` (vendor owner/admin rules)
- `GET/POST /api/orders/` (customer creates order)
- `GET /api/customer/orders/`
- `GET /api/customer/orders/{id}/`
- `GET/POST/PUT/PATCH/DELETE /api/vendor/products/` (vendor own products)
- `GET/PUT/PATCH/DELETE /api/admin/users/{id}/` (admin)

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Configure PostgreSQL env vars:
- `POSTGRES_DB`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_HOST`
- `POSTGRES_PORT`

Then run:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
