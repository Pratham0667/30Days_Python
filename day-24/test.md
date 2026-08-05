# Day 24 - NumPy, Random Numbers & Data Visualization

# 🎯 Topics Covered

- Introduction to NumPy
- NumPy Version
- Creating NumPy Arrays
- Data Types in NumPy
- Shape of Arrays
- Mathematical Operations
- Random Number Generation
- Normal Distribution
- Array Statistics
- SciPy Statistics Module
- Data Visualization using Matplotlib
- Histograms
- Line Graphs
- Seaborn Themes

---

# 📚 Introduction

**NumPy (Numerical Python)** is one of the most important Python libraries for scientific computing.

It provides:

- Fast numerical calculations
- Multi-dimensional arrays
- Mathematical functions
- Random number generation
- Statistical operations

Many Python libraries like:

- Pandas
- Matplotlib
- SciPy
- TensorFlow
- PyTorch

are built using NumPy.

---

# 1. Importing Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

### Purpose

- `numpy` → Numerical computing
- `matplotlib.pyplot` → Plotting graphs
- `seaborn` → Better graph styling

---

# 2. Checking NumPy Version

```python
print(np.__version__)
```

Displays the installed NumPy version.

Example:

```
2.5.1
```

---

# 3. Listing NumPy Functions

```python
print(dir(np))
```

Displays every available NumPy function.

Useful for exploring the library.

---

# 4. Creating NumPy Arrays

## Integer Array

```python
python_list = [1,2,3,4,5]

numpy_array = np.array(python_list)
```

Output

```
[1 2 3 4 5]
```

---

## Float Array

```python
np.array([1,2,3,4,5], dtype=float)
```

Output

```
[1. 2. 3. 4. 5.]
```

---

## Boolean Array

```python
np.array([0,1,-1,0,0], dtype=bool)
```

Output

```
[False True True False False]
```

---

# 5. Multi-dimensional Arrays

```python
two_dimension_array = np.array([
    (1,2,3),
    (4,5,6),
    (7,8,9)
])
```

Output

```
[[1 2 3]
 [4 5 6]
 [7 8 9]]
```

---

# 6. Shape of Arrays

The shape tells the number of rows and columns.

Example

```python
nums.shape
```

Output

```
(5,)
```

Means

- 1-dimensional
- 5 elements

---

Example

```python
three_by_four_array.shape
```

Output

```
(3,4)
```

Meaning

- 3 rows
- 4 columns

---

# 7. Mathematical Operations

NumPy performs operations on every element.

---

## Addition

```python
array + 10
```

---

## Subtraction

```python
array - 10
```

---

## Multiplication

```python
array * 10
```

---

## Division

```python
array / 10
```

---

## Modulus

```python
array % 3
```

Returns remainder.

---

## Floor Division

```python
array // 10
```

Returns integer quotient.

---

## Exponent

```python
array ** 2
```

Squares every element.

---

# 8. Random Numbers

## Random Float

```python
np.random.random()
```

Generates one random number between

```
0
```

and

```
1
```

---

# 9. Normal Distribution

Syntax

```python
np.random.normal(mean, standard_deviation, size)
```

Example

```python
normal_array = np.random.normal(79,15,80)
```

Meaning

- Mean = 79
- Standard deviation = 15
- Total numbers = 80

---

Another Example

```python
np.random.normal(5,0.5,1000)
```

Creates 1000 random numbers around 5.

---

# 10. Descriptive Statistics

For arrays:

## Minimum

```python
array.min()
```

or

```python
np.min(array)
```

---

## Maximum

```python
array.max()
```

---

## Mean

```python
array.mean()
```

or

```python
np.mean(array)
```

---

## Median

```python
np.median(array)
```

---

## Standard Deviation

```python
array.std()
```

---

## Mode (SciPy)

```python
from scipy import stats

stats.mode(array)
```

Returns the most frequently occurring value.

---

# 11. SciPy Statistics Module

```python
from scipy import stats
```

Provides advanced statistical functions like

- Mode
- Correlation
- Probability distributions
- Statistical tests

---

# 12. Histograms

A histogram shows how data is distributed.

Example

```python
plt.hist(normal_array,
         color="grey",
         bins=50)
```

Parameters

- color
- bins

---

Another Example

```python
plt.hist(np_normal_dis,
         color="grey",
         bins=21)
```

---

Display graph

```python
plt.show()
```

---

# 13. Seaborn Theme

Instead of the old

```python
sns.set()
```

use

```python
sns.set_theme()
```

It applies modern styling to plots.

---

# 14. Line Plot

Example

```python
temp = np.array([1,2,3,4,5])

pressure = temp*2 + 5

plt.plot(temp, pressure)
```

Output

A Temperature vs Pressure graph.

---

# 15. Labels

## X-axis

```python
plt.xlabel("Temperature in oC")
```

---

## Y-axis

```python
plt.ylabel("Pressure in atm")
```

---

## Title

```python
plt.title("Temperature vs Pressure")
```

---

## Custom X-axis Marks

```python
plt.xticks(np.arange(0,6,0.5))
```

Creates tick marks

```
0
0.5
1
1.5
...
6
```

---

# 16. Display Plot

```python
plt.show()
```

Without this, graphs may not appear in a Python script.

---

# 📊 Workflow

```
Python List
      │
      ▼
NumPy Array
      │
      ▼
Mathematical Operations
      │
      ▼
Random Numbers
      │
      ▼
Statistics
      │
      ▼
Visualization
```

---

# 📌 Common NumPy Functions

| Function | Purpose |
|----------|----------|
| np.array() | Create array |
| np.min() | Minimum |
| np.max() | Maximum |
| np.mean() | Average |
| np.median() | Median |
| np.std() | Standard deviation |
| np.random.random() | Random float |
| np.random.normal() | Normal distribution |
| np.arange() | Range of values |

---

# 📌 Matplotlib Functions

| Function | Purpose |
|----------|----------|
| plt.plot() | Line graph |
| plt.hist() | Histogram |
| plt.xlabel() | X-axis label |
| plt.ylabel() | Y-axis label |
| plt.title() | Graph title |
| plt.xticks() | Tick positions |
| plt.show() | Display graph |

---

# 📌 Seaborn Function

```python
sns.set_theme()
```

Applies a clean and attractive theme to graphs.

---

# ⚠️ Common Mistakes

### Forgetting NumPy alias

❌

```python
import numpy

np.array()
```

✅

```python
import numpy as np
```

---

### Incorrect Median Call

❌

```python
array.median()
```

NumPy arrays do **not** have a `.median()` method.

✅

```python
np.median(array)
```

---

### Forgetting `plt.show()`

Graphs won't display in scripts.

Always use

```python
plt.show()
```

---

### Using Deprecated Seaborn Method

Old

```python
sns.set()
```

New

```python
sns.set_theme()
```

---

# 🚀 Skills Practiced

- Creating NumPy arrays
- Working with data types
- Multi-dimensional arrays
- Finding array shape
- Mathematical operations
- Generating random numbers
- Normal distributions
- Descriptive statistics
- Using SciPy
- Creating histograms
- Creating line graphs
- Customizing graph appearance
- Using Seaborn themes

---

# 📝 Key Takeaways

- NumPy is the foundation of scientific computing in Python.
- Arrays are faster and more efficient than Python lists for numerical operations.
- NumPy supports vectorized mathematical operations.
- `np.random.normal()` generates data following a normal distribution.
- Use `np.min()`, `np.max()`, `np.mean()`, `np.median()`, and `np.std()` for statistical analysis.
- SciPy provides additional statistical functions like `stats.mode()`.
- Matplotlib is used to create visualizations such as histograms and line plots.
- Seaborn improves the appearance of plots with themes.

---

# 💡 Reflection

Today I learned how to use NumPy for numerical computing, including creating arrays, performing element-wise mathematical operations, generating random values, and calculating descriptive statistics. I also explored SciPy for statistical analysis and used Matplotlib with Seaborn to visualize data through histograms and line graphs. These tools form the foundation of Python's data analysis and scientific computing ecosystem.