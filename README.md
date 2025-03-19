# Product Inventory Management API

## Overview
This is a web-based **Product Inventory Management System** built using **Django** and **Django REST Framework (DRF)**. It provides an API to manage products and a user-friendly frontend to interact with the inventory.

## Features
- **API Endpoints** for managing products (list, add, update, delete)
- **Frontend (Django Templates)** to display and manage products
- **AJAX Integration** for seamless CRUD operations
- **Bootstrap Styling** for a modern UI
- **Validation** to prevent negative prices

---

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, Bootstrap, JavaScript (AJAX, jQuery)
- **Database:** SQLite (default, can be changed to PostgreSQL/MySQL)

---

## Installation & Setup

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/django-product-inventory.git
cd django-product-inventory


2. Create a Virtual Environment & Install Dependencies
python -m venv venv
On Windows use: venv\Scripts\activate
pip install django djangorestframework

3. Run Migrations
python manage.py migrate

4. Run the Development Server
python manage.py runserver

Now, open http://127.0.0.1:8000/ in your browser.


Frontend Features
Product List: Displays all products.
Add Product: A form to add new products.
Update Product: Inline editing for price and stock.
Delete Product: Remove products with confirmation.
AJAX Implementation: Ensures a smooth user experience.
