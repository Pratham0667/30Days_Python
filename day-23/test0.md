# Day 23 - Python Virtual Environment (venv) & Flask Setup

# 🎯 Topics Covered

- What is a Virtual Environment?
- Installing `virtualenv`
- Creating a Virtual Environment
- Activating the Virtual Environment
- Installing Packages inside venv
- Upgrading `pip`
- Using `pip freeze`
- Checking Installed Packages
- Git Status
- Deactivating the Virtual Environment

---

# 📚 Introduction

A **Virtual Environment (venv)** is an isolated Python environment that allows each project to have its own Python packages and dependencies.

Benefits:

- Prevents version conflicts
- Keeps projects independent
- Easier collaboration
- Easier deployment
- Cleaner package management

---

# 1. Installing virtualenv

Install the package:

```bash
pip install virtualenv
```

This installs the tool required to create virtual environments. 

---

# 2. Creating a Virtual Environment

Command:

```bash
python -m venv venv
```

Explanation:

- `python` → Python interpreter
- `-m` → Run a module
- `venv` → Python's built-in virtual environment module
- Last `venv` → Folder name where the environment is created

Directory created:

```
30Days_Python/
│
├── Day01
├── Day02
├── ...
├── Day23
├── venv/
```

Inside the `venv` folder, Python creates:

```
venv/
│
├── Scripts/
├── Include/
├── Lib/
├── pyvenv.cfg
```

---

# 3. Activating the Virtual Environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

After activation, the terminal changes from:

```
PS C:\Project>
```

to

```
(venv) PS C:\Project>
```

The `(venv)` prefix indicates that all Python and pip commands now operate inside the virtual environment.

---

# 4. Installing Flask

Install Flask inside the active virtual environment:

```bash
pip install Flask
```

Flask automatically installs several dependencies:

- Flask
- Werkzeug
- Jinja2
- Click
- Blinker
- ItsDangerous
- MarkupSafe
- Colorama (Windows)

These packages are stored only inside the `venv` folder and do not affect the global Python installation. 

---

# 5. Upgrading pip

Upgrade pip to the latest version:

```bash
python.exe -m pip install --upgrade pip
```

Why upgrade?

- Latest features
- Bug fixes
- Better package compatibility
- Improved security

---

# 6. Viewing Installed Packages

Use:

```bash
pip freeze
```

Example output:

```text
Flask==3.1.3
Werkzeug==3.1.8
Jinja2==3.1.6
Click==8.1.3
Blinker==1.9.0
MarkupSafe==3.0.3
ItsDangerous==2.2.0
Colorama==0.4.6
```

`pip freeze` lists every installed package along with its exact version.

This output is commonly saved to a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

This makes it easy to recreate the same environment later.

---

# 7. Deactivating the Virtual Environment

When finished:

```bash
deactivate
```

The `(venv)` prefix disappears, returning you to the global Python environment. 

---

# 📝 Common Commands

### Install virtualenv

```bash
pip install virtualenv
```

---

### Create environment

```bash
python -m venv venv
```

---

### Activate (Windows)

```powershell
.\venv\Scripts\Activate
```

---

### Install Flask

```bash
pip install Flask
```

---

### Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

### List installed packages

```bash
pip freeze
```

---

### Save requirements

```bash
pip freeze > requirements.txt
```

---

### Exit virtual environment

```bash
deactivate
```

---

# 📦 Flask Dependency Tree

```
Flask
│
├── Werkzeug
├── Jinja2
├── Click
├── Blinker
├── ItsDangerous
├── MarkupSafe
└── Colorama (Windows)
```

---

# 📂 Project Structure

```
30Days_Python/
│
├── Day01
├── Day02
├── ...
├── Day23
│   └── notes.md
│
├── venv/
│   ├── Scripts/
│   ├── Include/
│   ├── Lib/
│   └── pyvenv.cfg
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# ⚠️ Common Mistakes

### Activating with the wrong path

❌ Wrong

```powershell
.\venv\Script\Activate
```

✅ Correct

```powershell
.\venv\Scripts\Activate
```

---

### Forgetting to activate

If you install packages before activating:

```bash
pip install Flask
```

they may be installed globally instead of inside the virtual environment.

---

### Committing the `venv` folder

Never upload your virtual environment to GitHub.

Instead, add it to `.gitignore`:

```
venv/
```

Only commit your source code and `requirements.txt`.

---

# 📌 Key Takeaways

- A virtual environment isolates project dependencies.
- `python -m venv venv` creates a new environment.
- Activate it before installing packages.
- `pip install Flask` installs Flask and its required dependencies.
- `pip freeze` displays all installed packages and versions.
- `requirements.txt` can be generated using `pip freeze`.
- `deactivate` exits the virtual environment.

---

# 🚀 Skills Practiced

- Creating a virtual environment
- Activating and deactivating venv
- Installing Python packages
- Managing project dependencies
- Upgrading pip
- Using `pip freeze`
- Understanding Flask dependencies
- Organizing Python project environments

---

# 💡 Reflection

Today I learned how to create and manage a Python Virtual Environment using `venv`. I practiced activating and deactivating the environment, installing Flask and its dependencies, upgrading `pip`, checking installed packages with `pip freeze`, and verifying my Git repository status. Using virtual environments is an essential practice for keeping Python projects organized, isolated, and easy to share with others.
