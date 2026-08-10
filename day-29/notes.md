# Day 29 - Building REST API with Flask & MongoDB

# 🎯 Topics Covered

- Introduction to REST APIs
- Flask Web Framework
- API Endpoints
- HTTP Methods
- GET Requests
- POST Requests
- PUT Requests
- DELETE Requests
- Flask and MongoDB Integration
- PyMongo
- MongoDB ObjectId
- CRUD Operations
- Testing APIs using cURL
- Testing API responses in the browser
- Running a local Flask server

---

# 📚 Introduction

An **API (Application Programming Interface)** allows different software applications to communicate with each other.

A **REST API** uses HTTP methods to perform operations on resources.

In this project, Flask is used to create the backend API and MongoDB is used as the database.

The API manages student information stored in a MongoDB collection.

---

# 1. Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming language |
| Flask | Web framework |
| MongoDB | NoSQL database |
| PyMongo | Connects Python with MongoDB |
| cURL | Testing API requests |

---

# 2. Flask

**Flask** is a lightweight Python web framework used to build web applications and REST APIs.

Import Flask:

```python
from flask import Flask
```

Create the Flask application:

```python
app = Flask(__name__)
```

---

# 3. Running the Flask Application

Start the Flask application using:

```bash
python build_API.py
```

The development server runs locally at:

```text
http://127.0.0.1:5000
```

or:

```text
http://localhost:5000
```

---

# 4. API Base URL

The API created in this project uses:

```text
http://127.0.0.1:5000/api/v1.0/students
```

The same endpoint can be opened in a browser:

```text
http://localhost:5000/api/v1.0/students
```

**Run this URL in the browser to see the API output.**

---

# 5. REST API

REST stands for:

**Representational State Transfer**

A REST API uses HTTP methods to interact with resources.

| HTTP Method | Operation |
|-------------|-----------|
| GET | Read data |
| POST | Create data |
| PUT | Update data |
| DELETE | Delete data |

---

# 6. API Resource

The main resource in this project is:

```text
students
```

The API endpoint is:

```text
/api/v1.0/students
```

A specific student can be accessed using their MongoDB ID:

```text
/api/v1.0/students/<id>
```

---

# 7. MongoDB Connection

PyMongo is used to connect Python with MongoDB.

```python
import pymongo
```

A MongoDB connection is created using:

```python
client = pymongo.MongoClient(MONGODB_URI)
```

The database is selected using:

```python
db = client['thirty_days_of_python']
```

The student collection is accessed using:

```python
db.students
```

---

# 8. Environment Variables

The MongoDB connection string is stored in an environment variable instead of directly writing it in the Python code.

Example:

```text
MONGODB_URI=your_mongodb_connection_string
```

The environment variable can be loaded using:

```python
import os

MONGODB_URI = os.getenv("MONGODB_URI")
```

This keeps sensitive connection information outside the source code.

---

# 9. Student Data

Each student is stored as a MongoDB document.

Example:

```python
{
    "name": "Anvesha",
    "country": "India",
    "city": "Mangalore",
    "age": 20
}
```

MongoDB automatically creates an `_id` field for each document.

Example:

```text
_id: ObjectId('6a76ef3da1be5a15203b6509')
```

---

# 10. GET - Retrieve All Students

The GET endpoint retrieves all students.

```text
GET /api/v1.0/students
```

Example URL:

```text
http://127.0.0.1:5000/api/v1.0/students
```

The endpoint returns the student records.

---

# 11. GET - Get a Specific Student

A specific student can be retrieved using their MongoDB ID.

```text
GET /api/v1.0/students/<id>
```

Example using cURL:

```bash
curl.exe -X GET http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE
```

Replace:

```text
PASTE_ID_HERE
```

with the student's actual MongoDB `_id`.

Example:

```bash
curl.exe -X GET http://127.0.0.1:5000/api/v1.0/students/6a76ef3da1be5a15203b6509
```

---

# 12. POST - Add a New Student

The **POST** method is used to create a new student.

```text
POST /api/v1.0/students
```

Example using cURL:

```bash
curl.exe -X POST http://127.0.0.1:5000/api/v1.0/students -d "name=Anvesha" -d "country=India" -d "city=Mangalore" -d "skills=Python, Flask, MongoDB" -d "bio=Computer Science student" -d "birthyear=2006"
```

The API receives the student information and inserts it into MongoDB.

---

# 13. POST Data Fields

The student data can contain:

```text
name
country
city
skills
bio
birthyear
```

Example:

```text
name=Anvesha
country=India
city=Mangalore
skills=Python, Flask, MongoDB
bio=Computer Science student
birthyear=2006
```

The skills can be converted into a list using:

```python
request.form['skills'].split(', ')
```

Input:

```text
Python, Flask, MongoDB
```

Output:

```python
['Python', 'Flask', 'MongoDB']
```

---

# 14. PUT - Update a Student

The **PUT** method is used to update an existing student.

```text
PUT /api/v1.0/students/<id>
```

Example:

```bash
curl.exe -X PUT http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE -d "name=Anvesha" -d "country=India" -d "city=Mangalore" -d "skills=Python, Flask, MongoDB, API" -d "bio=Computer Science and Design Engineering student" -d "birthyear=2006"
```

Replace:

```text
PASTE_ID_HERE
```

with the student's MongoDB `_id`.

---

# 15. MongoDB Update Operation

The PUT operation uses MongoDB's:

```python
update_one()
```

The document can be updated using:

```python
{
    "$set": student
}
```

This updates the existing student document with the new values.

---

# 16. DELETE - Delete a Student

The **DELETE** method removes a student from the database.

```text
DELETE /api/v1.0/students/<id>
```

Example:

```bash
curl.exe -X DELETE http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE
```

Replace:

```text
PASTE_ID_HERE
```

with the student's MongoDB `_id`.

Example:

```bash
curl.exe -X DELETE http://127.0.0.1:5000/api/v1.0/students/6a76ef3da1be5a15203b6509
```

---

# 17. MongoDB Delete Operation

The DELETE operation uses:

```python
delete_one()
```

The document is selected using its MongoDB ObjectId.

```python
db.students.delete_one({
    "_id": ObjectId(id)
})
```

---

# 18. MongoDB ObjectId

MongoDB automatically generates a unique `_id` for every document.

Example:

```text
ObjectId('6a76ef3da1be5a15203b6509')
```

When working with a student ID in the Flask API, it needs to be converted into an `ObjectId`.

```python
from bson.objectid import ObjectId
```

Example:

```python
ObjectId(id)
```

This allows MongoDB to identify the correct document.

---

# 19. CRUD Operations

CRUD stands for:

- **C** → Create
- **R** → Read
- **U** → Update
- **D** → Delete

The API implements CRUD operations using HTTP methods.

| CRUD Operation | HTTP Method | Endpoint |
|----------------|-------------|----------|
| Create | POST | `/students` |
| Read All | GET | `/students` |
| Read One | GET | `/students/<id>` |
| Update | PUT | `/students/<id>` |
| Delete | DELETE | `/students/<id>` |

---

# 20. Testing the API Using cURL

cURL is a command-line tool used to send HTTP requests.

On Windows, use:

```bash
curl.exe
```

The API must be running before executing these commands.

Start the Flask server:

```bash
python build_API.py
```

---

# 21. cURL - Get All Students

```bash
curl.exe -X GET http://127.0.0.1:5000/api/v1.0/students
```

This retrieves all students.

---

# 22. cURL - Get a Specific Student

```bash
curl.exe -X GET http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE
```

Replace `PASTE_ID_HERE` with the MongoDB `_id`.

---

# 23. cURL - Add a Student

```bash
curl.exe -X POST http://127.0.0.1:5000/api/v1.0/students -d "name=Anvesha" -d "country=India" -d "city=Mangalore" -d "skills=Python, Flask, MongoDB" -d "bio=Computer Science student" -d "birthyear=2006"
```

This creates a new student document.

---

# 24. cURL - Update a Student

```bash
curl.exe -X PUT http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE -d "name=Anvesha" -d "country=India" -d "city=Mangalore" -d "skills=Python, Flask, MongoDB, API" -d "bio=Computer Science student" -d "birthyear=2006"
```

This updates the selected student.

---

# 25. cURL - Delete a Student

```bash
curl.exe -X DELETE http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE
```

This removes the selected student.

---

# 26. Complete cURL Cheat Sheet

### Get All Students

```bash
curl.exe -X GET http://127.0.0.1:5000/api/v1.0/students
```

### Get Specific Student

```bash
curl.exe -X GET http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE
```

### Add Student

```bash
curl.exe -X POST http://127.0.0.1:5000/api/v1.0/students -d "name=Anvesha" -d "country=India" -d "city=Mangalore" -d "skills=Python, Flask, MongoDB" -d "bio=Computer Science student" -d "birthyear=2006"
```

### Update Student

```bash
curl.exe -X PUT http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE -d "name=Anvesha" -d "country=India" -d "city=Mangalore" -d "skills=Python, Flask, MongoDB, API" -d "bio=Computer Science student" -d "birthyear=2006"
```

### Delete Student

```bash
curl.exe -X DELETE http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE
```

---

# 27. Testing Workflow

A complete CRUD test can be performed in the following order:

```text
GET
 ↓
View all students
 ↓
POST
 ↓
Create a new student
 ↓
GET
 ↓
Find the newly created student
 ↓
PUT
 ↓
Update the student
 ↓
GET
 ↓
Verify the updated information
 ↓
DELETE
 ↓
Delete the student
 ↓
GET
 ↓
Verify that the student was removed
```

---

# 28. API and MongoDB Workflow

```text
Client / cURL / Browser
          │
          ▼
      Flask API
          │
          ▼
     HTTP Request
          │
          ▼
     API Endpoint
          │
          ▼
        PyMongo
          │
          ▼
       MongoDB
          │
          ▼
     Student Data
          │
          ▼
     JSON Response
```

---

# 29. API Endpoint Summary

| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | `/api/v1.0/students` | Get all students |
| GET | `/api/v1.0/students/<id>` | Get one student |
| POST | `/api/v1.0/students` | Add a student |
| PUT | `/api/v1.0/students/<id>` | Update a student |
| DELETE | `/api/v1.0/students/<id>` | Delete a student |

---

# 30. Important Concepts

### Flask

Python web framework used to build the API.

### REST API

Architecture that allows applications to communicate using HTTP.

### HTTP Methods

Used to specify what operation should be performed.

### PyMongo

Python driver used to communicate with MongoDB.

### MongoDB

NoSQL database used to store student documents.

### ObjectId

MongoDB's unique identifier for documents.

### cURL

Command-line tool used to test HTTP requests.

---

# ⚠️ Common Mistakes

### 1. Flask server is not running

If the server is not running, cURL cannot connect to the API.

Start it using:

```bash
python build_API.py
```

---

### 2. Incorrect URL

❌

```text
http://127.0.0.1:5000/students
```

✅

```text
http://127.0.0.1:5000/api/v1.0/students
```

---

### 3. Forgetting the Student ID

For GET, PUT and DELETE operations on a specific student, the MongoDB ID is required.

```bash
curl.exe -X DELETE http://127.0.0.1:5000/api/v1.0/students/PASTE_ID_HERE
```

---

### 4. Using the Wrong HTTP Method

```text
GET     → Read
POST    → Create
PUT     → Update
DELETE  → Delete
```

---

### 5. Invalid MongoDB ID

The ID must be a valid MongoDB ObjectId.

Example:

```text
6a76ef3da1be5a15203b6509
```

---

# 🚀 Skills Practiced

- Building REST APIs with Flask
- Creating API endpoints
- Working with HTTP methods
- Connecting Flask with MongoDB
- Using PyMongo
- Performing MongoDB CRUD operations
- Working with ObjectId
- Handling API data
- Returning API responses
- Testing APIs with cURL
- Testing APIs through a browser
- Managing environment variables
- Running a local backend server

---

# 📌 Key Takeaways

- Flask can be used to build lightweight REST APIs.
- REST APIs use HTTP methods to perform different operations.
- `GET` is used to retrieve data.
- `POST` is used to create new data.
- `PUT` is used to update existing data.
- `DELETE` is used to remove data.
- PyMongo allows Python applications to communicate with MongoDB.
- MongoDB documents have a unique `_id`.
- `ObjectId` is used to identify MongoDB documents.
- cURL can be used to test APIs directly from the terminal.
- A browser can be used to test GET endpoints.
- Environment variables can be used to keep database connection information separate from source code.

---

# 💡 Reflection

Today I learned how to build and test a REST API using **Flask and MongoDB**. I practiced connecting a Python application to MongoDB using **PyMongo**, creating API endpoints, and implementing complete **CRUD operations**.

I also learned how to test the API using `curl.exe`, including retrieving all students, retrieving a specific student, adding a new student, updating an existing student, and deleting a student.

This helped me understand how a client can communicate with a backend API and how the backend interacts with a database to manage data.