# Day 27 - Python with MongoDB

# 🎯 Topics Covered

- Introduction to MongoDB
- MongoDB Atlas
- MongoDB Compass
- Connecting Python with MongoDB
- PyMongo
- Installing PyMongo
- Installing `dnspython`
- Using `python-dotenv`
- Environment variables
- MongoDB connection URI
- Creating and accessing databases
- Creating collections
- Inserting documents
- Working with MongoDB documents
- Retrieving documents
- Verifying data using MongoDB Atlas and Compass
- Using `.gitignore` for sensitive files

---

# 📚 Introduction

**MongoDB** is a NoSQL database that stores data in flexible, JSON-like documents instead of traditional rows and columns.

MongoDB organizes data using:

```text
Database
   │
   └── Collection
          │
          ├── Document
          ├── Document
          └── Document
```

In this practice, Python was connected to MongoDB using the **PyMongo** library.

---

# 1. Installing Required Libraries

The following packages were installed for the project:

```bash
pip install pymongo
pip install dnspython
pip install python-dotenv
```

### Purpose of the Libraries

| Library | Purpose |
|--------|---------|
| `pymongo` | Connect Python with MongoDB |
| `dnspython` | Required for MongoDB DNS connection strings |
| `python-dotenv` | Load environment variables from `.env` |

---

# 2. Creating a Virtual Environment

A virtual environment was created to keep the project dependencies isolated.

```bash
python -m venv venv
```

Activate the virtual environment in PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, the terminal displays:

```text
(venv)
```

This indicates that the virtual environment is active.

---

# 3. Importing Required Modules

The Python program uses the following imports:

```python
import os
import pymongo
from dotenv import load_dotenv
```

### Purpose

- `os` → Access environment variables.
- `pymongo` → Connect and interact with MongoDB.
- `load_dotenv` → Load variables stored in the `.env` file.

---

# 4. Loading Environment Variables

The `.env` file was used to store the MongoDB connection string.

```python
load_dotenv()
```

The MongoDB URI was accessed using:

```python
MONGODB_URI = os.getenv("MONGODB_URI")
```

This keeps the connection string separate from the Python source code.

---

# 5. MongoDB Connection

The MongoDB client was created using PyMongo:

```python
client = pymongo.MongoClient(MONGODB_URI)
```

The `MongoClient` establishes the connection between Python and MongoDB.

---

# 6. Listing Databases

The available databases were displayed using:

```python
print(client.list_database_names())
```

The output included databases such as:

```text
['sample_mflix', 'thirty_days_of_python', 'admin', 'local']
```

This confirmed that the Python program successfully connected to MongoDB.

---

# 7. Selecting a Database

The database used for this practice was:

```python
db = client["thirty_days_of_python"]
```

The database name is:

```text
thirty_days_of_python
```

---

# 8. MongoDB Collections

A collection is similar to a table in a relational database, but MongoDB stores documents instead of rows.

The collection used in this project was:

```text
students
```

The overall structure was:

```text
thirty_days_of_python
        │
        └── students
                │
                ├── Document
                ├── Document
                └── Document
```

---

# 9. Creating Student Documents

A list of student documents was created in Python.

```python
students = [
    {
        'name': 'Anvesha',
        'country': 'India',
        'city': 'Mangalore',
        'age': 20
    },

    {
        'name': 'Pratham',
        'country': 'India',
        'city': 'Mangalore',
        'age': 20
    },

    {
        'name': 'Sami',
        'country': 'Finland',
        'city': 'Helsinki',
        'age': 25
    }
]
```

Each dictionary represents one MongoDB document.

---

# 10. Inserting Documents

The student documents were inserted into the `students` collection.

```python
for student in students:
    db.students.insert_one(student)
```

### `insert_one()`

The `insert_one()` method inserts a single document into a MongoDB collection.

Since the program loops through the list, each student is inserted individually.

---

# 11. MongoDB Documents

After insertion, MongoDB automatically assigns an `_id` to each document.

Example:

```text
{
    "_id": ObjectId("..."),
    "name": "Anvesha",
    "country": "India",
    "city": "Mangalore",
    "age": 20
}
```

The `_id` field uniquely identifies the document.

---

# 12. Retrieving Documents

Documents from the collection can be retrieved using:

```python
db.students.find()
```

The returned documents can be displayed using a loop:

```python
for student in db.students.find():
    print(student)
```

This allows the inserted records to be viewed from Python.

---

# 13. MongoDB Atlas

**MongoDB Atlas** was used as the cloud database platform.

The database created for the project was:

```text
thirty_days_of_python
```

The collection was:

```text
students
```

The inserted student documents were verified through the MongoDB Atlas Data Explorer.

---

# 14. MongoDB Compass

The same MongoDB database was also viewed using **MongoDB Compass**.

MongoDB Compass provides a graphical interface for working with:

- Databases
- Collections
- Documents
- Queries
- Indexes
- Schema information

The `students` collection was successfully displayed in Compass.

---

# 15. Database Verification

The connection was verified from Python using:

```python
print(client.list_database_names())
```

The inserted documents were also visible in MongoDB Atlas and MongoDB Compass.

This confirmed the workflow:

```text
Python
   │
   ▼
PyMongo
   │
   ▼
MongoDB Atlas
   │
   ▼
thirty_days_of_python
   │
   ▼
students
   │
   ▼
Documents
```

---

# 16. Environment Variables

The MongoDB URI contains connection information and should not be directly exposed in source code.

Instead, it was stored in:

```text
.env
```

Example:

```env
MONGODB_URI=your_mongodb_connection_string
```

Python accesses it using:

```python
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
```

---

# 17. `.gitignore`

Sensitive and unnecessary files should not be committed to GitHub.

The project uses `.gitignore` to exclude files such as:

```text
.env
venv/
```

### Why?

- `.env` may contain database credentials or connection strings.
- `venv/` contains the local Python virtual environment and does not need to be uploaded.

---

# 18. Project Structure

The Day 27 project was organized as:

```text
Day27/
│
├── mongodb_practice.py
├── instructions.md
├── .env
├── .gitignore
└── venv/
```

The virtual environment remains local and should be excluded from GitHub.

---

# 📌 Important PyMongo Methods

| Method | Purpose |
|--------|---------|
| `pymongo.MongoClient()` | Connect to MongoDB |
| `list_database_names()` | List available databases |
| `insert_one()` | Insert one document |
| `find()` | Retrieve documents |
| `find_one()` | Retrieve one document |

---

# 📌 MongoDB Terminology

| MongoDB | Relational Database |
|---------|---------------------|
| Database | Database |
| Collection | Table |
| Document | Row |
| Field | Column |
| `_id` | Primary key |

MongoDB stores documents in a flexible, JSON-like structure.

---

# ⚠️ Common Mistakes

### 1. Forgetting to Install PyMongo

❌

```python
import pymongo
```

without installing the package.

✅

```bash
pip install pymongo
```

---

### 2. Forgetting `dnspython`

MongoDB Atlas connection strings may require DNS support.

Install it using:

```bash
pip install dnspython
```

---

### 3. Hardcoding the MongoDB URI

❌

```python
MONGODB_URI = "your_connection_string"
```

✅

Store it in `.env`:

```env
MONGODB_URI=your_connection_string
```

and load it using:

```python
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
```

---

### 4. Forgetting to Load `.env`

❌

```python
MONGODB_URI = os.getenv("MONGODB_URI")
```

without loading the environment file.

✅

```python
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
```

---

### 5. Uploading `.env` to GitHub

Never commit the `.env` file when it contains sensitive connection information.

Add:

```text
.env
```

to `.gitignore`.

---

### 6. Forgetting to Activate the Virtual Environment

Before installing or running project dependencies:

```powershell
.\venv\Scripts\Activate.ps1
```

The terminal should show:

```text
(venv)
```

---

# 🧪 Flask Experiment

During the practice, Flask was initially experimented with.

However, no Flask application route was required for the MongoDB exercise.

Running Flask without a defined route resulted in:

```text
404 Not Found
```

Therefore, the Flask-related code was removed from the final implementation.

The final Day 27 project focuses on:

```text
Python + PyMongo + MongoDB
```

---

# 📊 Practical Workflow

```text
Create Virtual Environment
          │
          ▼
Install PyMongo & Dependencies
          │
          ▼
Create .env
          │
          ▼
Load MongoDB URI
          │
          ▼
Create MongoClient
          │
          ▼
Connect to Database
          │
          ▼
Create / Access Collection
          │
          ▼
Insert Documents
          │
          ▼
Retrieve Documents
          │
          ▼
Verify in MongoDB Atlas / Compass
```

---

# 🚀 Skills Practiced

- Creating Python virtual environments
- Installing Python packages
- Working with PyMongo
- Connecting Python to MongoDB
- Using MongoDB Atlas
- Using MongoDB Compass
- Creating databases and collections
- Creating MongoDB documents
- Inserting documents
- Retrieving documents
- Using environment variables
- Managing `.env` files
- Using `.gitignore`
- Verifying database operations

---

# 📝 Key Takeaways

- MongoDB is a NoSQL database that stores data as documents.
- Documents are stored inside collections.
- PyMongo allows Python programs to communicate with MongoDB.
- `MongoClient()` is used to establish a MongoDB connection.
- `list_database_names()` can be used to view available databases.
- `insert_one()` inserts a document into a collection.
- `find()` retrieves documents from a collection.
- MongoDB automatically creates an `_id` for documents.
- MongoDB Atlas provides a cloud-based MongoDB environment.
- MongoDB Compass provides a graphical interface for managing MongoDB data.
- Environment variables can be used to protect sensitive connection information.
- `.env` should not be committed to GitHub.

---

# 💡 Reflection

Today I learned how to connect **Python with MongoDB using PyMongo** and work with a MongoDB database through Python. I practiced creating student documents, inserting them into a collection, retrieving the stored data, and verifying the results using **MongoDB Atlas and MongoDB Compass**.

I also learned the importance of using **virtual environments, environment variables, `.env` files, and `.gitignore`** when working with database connections and Python projects.

This practice introduced me to working with a **NoSQL database from Python**, which is an important foundation for building backend and full-stack applications.
