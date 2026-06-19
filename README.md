#  Flask JWT Authentication API

A secure RESTful Authentication API built using **Flask**, **SQLite**, **SQLAlchemy**, and **JWT (JSON Web Tokens)**. The API provides user registration, login, and protected profile endpoints with password hashing and token-based authentication.

---

##  Features

* User Registration
* User Login
* JWT-based Authentication
* Protected User Profile Endpoint
* Password Hashing using Werkzeug
* SQLite Database Integration
* Logging for Authentication Events
* Modular Project Structure using Flask Blueprints

---

##  Tech Stack

* Python 
* Flask 
* Flask-SQLAlchemy
* Flask-JWT-Extended
* SQLite 
* Werkzeug Security
* JSON REST API

---

## Project Structure

```text
login/
│
├── app/
│   ├── models/
│   │   └── user.py
│   ├── routes/
│   │   └── auth_routes.py
│   ├── __init__.py
│   ├── config.py
│   └── exceptions.py
│
├── instance/
│   └── users.db
│
├── create_db.py
├── run.py
└── README.md
```

---

## Database

This project uses **SQLite** to store user information.

### User Table Schema

| Field    | Type    | Description          |
| -------- | ------- | -------------------- |
| id       | INTEGER | Primary Key          |
| username | TEXT    | User's username      |
| email    | TEXT    | Unique email address |
| password | TEXT    | Hashed password      |

Passwords are securely stored using:

```python
generate_password_hash(password)
```

and verified using:

```python
check_password_hash(hashed_password, password)
```

---

## API Endpoints

### Register User

**Endpoint**

```http
POST /register
```

**Request Body**

```json
{
  "username": "adithya",
  "email": "adithya@example.com",
  "password": "mypassword123"
}
```

**Success Response**

```json
{
  "message": "User Registered Successfully"
}
```

Status Code: `201 Created`

**Possible Errors**

```json
{
  "error": "Username required"
}
```

```json
{
  "error": "Email already exists"
}
```

---

### Login User

**Endpoint**

```http
POST /login
```

**Request Body**

```json
{
  "email": "adithya@example.com",
  "password": "mypassword123"
}
```

**Success Response**

```json
{
  "access_token": "<jwt-token>"
}
```

Status Code: `200 OK`

**Invalid Credentials**

```json
{
  "error": "Invalid Credentials"
}
```

Status Code: `401 Unauthorized`

---

### Get User Profile

**Endpoint**

```http
GET /profile
```

**Headers**

```text
Authorization: Bearer <jwt-token>
```

**Success Response**

```json
{
  "message": "Authorized User",
  "user": {
    "id": 1,
    "username": "adithya",
    "email": "adithya@example.com"
  }
}
```

Status Code: `200 OK`

---

##  Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/flask-jwt-auth-api.git
cd flask-jwt-auth-api
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create the Database

```bash
python create_db.py
```

### Run the Application

```bash
python run.py
```

The server will start at:

```text
http://127.0.0.1:5000/
```

---

##  Testing with Postman

### Register

```http
POST http://127.0.0.1:5000/register
```

### Login

```http
POST http://127.0.0.1:5000/login
```

Copy the returned JWT token.

### Access Protected Route

```http
GET http://127.0.0.1:5000/profile
```

Add the header:

```text
Authorization: Bearer <your-jwt-token>
```

---

##  Required Packages

```bash
pip install flask
pip install flask-sqlalchemy
pip install flask-jwt-extended
pip install werkzeug
```


##  Author
Adithya .k.s

Built using Flask to practice authentication, password hashing, JWT implementation, database integration, and secure REST API development.
