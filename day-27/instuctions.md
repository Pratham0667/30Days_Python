# Python with MongoDB

This project demonstrates how to connect Python with MongoDB using **PyMongo** and perform basic MongoDB operations.

---

## 📁 Project Structure

```text
python_with_mongodb/
│
├── instructions.md
├── mongodb_practice.py
│
└── venv/
```

> The `venv` directory contains the project's virtual environment and should not be committed to GitHub.

---

## 🛠️ Prerequisites

Make sure the following are installed:

- Python 3
- MongoDB Atlas account
- Visual Studio Code (recommended)
- Git (optional)

---

## 1. Create a Virtual Environment

Open the terminal inside the project directory:

```powershell
python -m venv venv
```

---

## 2. Activate the Virtual Environment

### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(venv)
```

---

## 3. Install Required Packages

Install **PyMongo** and **dnspython**:

```powershell
pip install pymongo dnspython
```

### Verify PyMongo

```powershell
pip show pymongo
```

### Verify Installed Packages

```powershell
pip freeze
```

`dnspython` is required when using MongoDB connection strings that begin with `mongodb+srv://`. 

---

## 4. Set Up MongoDB Atlas

Create a free MongoDB Atlas cluster.

### Steps

1. Create or log in to your MongoDB Atlas account.
2. Create a free cluster.
3. Add a database user.
4. Set a secure username and password.
5. Configure network access for your development environment.
6. Select **Connect**.
7. Choose the **Python** driver.
8. Copy the MongoDB connection string.

MongoDB Atlas provides a connection URI that can be used by PyMongo to connect the Python application to the cluster.

---

## 5. Configure the MongoDB Connection

Your connection string will look similar to:

```text
mongodb+srv://<username>:<password>@<cluster-url>/<database>
```

Replace the placeholders with your own MongoDB credentials.

### ⚠️ Security

**Never commit your MongoDB username, password or connection URI containing credentials to GitHub.**

For a real project, store sensitive values in environment variables instead.

---

## 6. Run the Python Program

Make sure the virtual environment is activated:

```powershell
.\venv\Scripts\Activate.ps1
```

Then run:

```powershell
python mongodb_practice.py
```

---

## 7. MongoDB Operations Practiced

The project is based on the following MongoDB concepts:

### Connect to MongoDB

```python
client = pymongo.MongoClient(MONGODB_URI)
```

### Access a Database

```python
db = client["thirty_days_of_python"]
```

### Access a Collection

```python
students = db.students
```

### Insert One Document

```python
db.students.insert_one({
    "name": "Anvesha",
    "country": "India",
    "city": "Mangalore",
    "age": 20
})
```

### Insert Multiple Documents

```python
db.students.insert_many([
    {
        "name": "David",
        "country": "UK",
        "city": "London",
        "age": 34
    },
    {
        "name": "John",
        "country": "Sweden",
        "city": "Stockholm",
        "age": 28
    }
])
```

### Find One Document

```python
db.students.find_one()
```

### Find Multiple Documents

```python
db.students.find()
```

### Find Using a Query

```python
db.students.find({
    "country": "Finland"
})
```

### Query Using a Modifier

```python
db.students.find({
    "age": {"$gt": 30}
})
```

### Limit Results

```python
db.students.find().limit(3)
```

### Sort Results

Ascending:

```python
db.students.find().sort("name")
```

Descending:

```python
db.students.find().sort("name", -1)
```

These operations correspond to the MongoDB topics insertion, finding documents, queries, modifiers, limiting results and sorting.

---

## 🔄 Basic MongoDB Workflow

```text
Python Application
       │
       ▼
    PyMongo
       │
       ▼
 MongoDB Atlas
       │
       ▼
    Database
       │
       ▼
   Collection
       │
       ▼
   Documents
```

---

## 🧪 Verify the Connection

A simple way to verify the connection is:

```python
print(client.list_database_names())
```

If the connection is successful, MongoDB returns the databases available to the connected user. 

---

## 📌 Important Commands

| Command | Purpose |
|---|---|
| `python -m venv venv` | Create virtual environment |
| `.\venv\Scripts\Activate.ps1` | Activate virtual environment |
| `pip install pymongo dnspython` | Install MongoDB dependencies |
| `pip show pymongo` | Check PyMongo installation |
| `pip freeze` | View installed packages |
| `python mongodb_practice.py` | Run the project |

---

## ⚠️ Common Issues

### `ModuleNotFoundError: No module named 'pymongo'`

Make sure the virtual environment is activated:

```powershell
.\venv\Scripts\Activate.ps1
```

Then install PyMongo:

```powershell
pip install pymongo
```

---

### `ModuleNotFoundError: No module named 'dns'`

Install dnspython:

```powershell
pip install dnspython
```

---

### MongoDB Connection Error

Check:

- MongoDB Atlas cluster is running.
- Username is correct.
- Password is correct.
- Connection URI is correct.
- Network access allows your connection.
- The virtual environment is activated.

---

## 🔐 Security Checklist

Before pushing this project to GitHub:

- [ ] Do not commit MongoDB passwords.
- [ ] Do not commit private connection strings.
- [ ] Add `.env` to `.gitignore`.
- [ ] Add `venv/` to `.gitignore`.
- [ ] Use environment variables for credentials.

Example:

```text
MONGODB_URI=your_mongodb_connection_string
```

---
