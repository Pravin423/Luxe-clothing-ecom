![image](https://github.com/user-attachments/assets/c504e63b-bbe3-4243-b8cd-0e7b354a5833)# 🛍️ Luxe Clothing – Django E-commerce Web Application
## 🎯 Project Overview

**Luxe Clothing** is a fully functional E-commerce Clothing Platform developed using Django. 
The application is built with scalability, performance, and user experience in mind, providing seamless shopping functionality with real-time payment integration.

### ✅ Key Features

- Cart functionality with quantity management
- Secure checkout integrated with **Razorpay Payment Gateway**
- Admin dashboard for managing products, orders, and users
- User authentication (login/register) using Django's auth system
- Responsive UI using **Bootstrap 5**
- SQL database via Django ORM for reliable data storage

---

## 🛠️ Tech Stack

- **Framework:** Django (Python 3.x)
- **Frontend:** HTML5, CSS3, Bootstrap
- **Database:** SQL (SQLite3 during development) via Django ORM
- **Authentication:** Django’s built-in `auth` module
- **Payment Gateway:** Razorpay API integration
- **Admin Interface:** Django Admin
- **Session Management:** Django middleware for cart persistence

---

## 🚀 Getting Started

1. Clone the Repository
git clone https://github.com/Pravin423/Luxe-clothing-ecom.git
cd Luxe-clothing-ecom

2. Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
3. Install Dependencies
pip install -r requirements.txt

5. Run Migrations
python manage.py makemigrations
python manage.py migrate

7. Create Superuser
python manage.py createsuperuser

9. Run the Server
python manage.py runserver
Access the app at:

Frontend: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

🔐 Razorpay Integration
Sign up at Razorpay and generate API keys.

Add the keys to your settings.py:

python
RAZORPAY_API_KEY = 'your_key_here'
RAZORPAY_API_SECRET = 'your_secret_here'

📁 Project Structure
Luxe-clothing-ecom/
├── ecom/                   # Django app
├── templates/              # HTML Templates
├── static/                 # CSS, JS, and Images
├── db.sqlite3              # Development database
├── manage.py               # Django management tool
└── requirements.txt        # Dependencies list
📸 Screenshots
HOME PAGE-
![image](https://github.com/user-attachments/assets/1fe69de4-8e8e-4080-a83b-6e83bf6c93d9)
![image](https://github.com/user-attachments/assets/6721c8d1-e1f7-4bae-9f5c-e4b9d1246fa3)
![image](https://github.com/user-attachments/assets/9ec8fe95-4d55-47f8-8ef1-6916c2d6ac15)
![image](https://github.com/user-attachments/assets/d1da39ca-eab3-45c5-966e-6c6fb8fa8a34)
LOGIN PAGE-
![image](https://github.com/user-attachments/assets/4a35d1ea-aecf-447b-91d2-cce7c7a42ac0)
REGISTER PAGE-
![image](https://github.com/user-attachments/assets/5b733501-f9d8-4e9e-b05a-ff145c03e7af)
CART PAGE-
![image](https://github.com/user-attachments/assets/29be32a7-1399-4577-a4cb-41e098815f05)
PAYMENT GATEWAY-
![image](https://github.com/user-attachments/assets/1c17f00d-e514-449b-97c5-cf151c337504)
ADMIN DASHBOARD-
![image](https://github.com/user-attachments/assets/bbc1be60-ebe9-4b9c-ad2d-1fac92df9610)
![image](https://github.com/user-attachments/assets/0b3d6328-5dd8-484c-bd4c-c155088a54b2)














