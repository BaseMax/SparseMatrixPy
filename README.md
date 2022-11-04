# SparseMatrix Python (SparseMatrixPy)

A full-featured library in **Python** for working with **Sparse Matrix**.

## SparseMatrix Functions

**Public Methods:**

- `def from_matrix(matrix)`

**Object-based Methods:**

- `def __init__(self, rows, cols)`
- `def __getitem__(self, index)`
- `def __setitem__(self, index, value)`
- `def __add__(self, other)`
- `def __mul__(self, other)`
- `def __str__(self)`
- `def __repr__(self)`
- `def __eq__(self, other)`
- `def __ne__(self, other)`
- `def __hash__(self)`
- `def __iter__(self)`
- `def __contains__(self, value)`
- `def __len__(self)`
- `def __bool__(self)`
- `def __delitem__(self, index)`
- `def to_matrix(self)`

## SparseMatrix Examples

```python
# Define a sparse matrix
m1 = sm.SparseMatrix(3, 3)
m1[0, 0] = 1
m1[0, 1] = 2
m1[1, 1] = 3
m1[2, 2] = 4
print("M1 Sparse Matrix:")
print(m1)

# Define another sparse matrix
m2 = sm.SparseMatrix(3, 3)
m2[0, 1] = 5
m2[1, 0] = 6
m2[1, 2] = 7
m2[2, 0] = 8
print("M2 Sparse Matrix:")
print(m2)

# Add the two sparse matrices
m3 = m1 + m2
print("Addition of M1 and M2:")
print(m3)

# Multiply the two sparse matrices
m4 = m1 * m2
print("Multiplication of M1 and M2:")
print(m4)

# Check if a value is in the sparse matrix
print("Is 5 in M1?")
print(5 in m1, "\n")

# Iterate over the sparse matrix
print("Iterate over M1:")
for value in m1:
print(value)

# Check if two sparse matrices are equal
print("\nAre M1 and M2 equal?")
print(m1 == m2, "\n")

# Check if two sparse matrices are not equal
print("Are M1 and M3 not equal?")
print(m1 != m3, "\n")

# Length of the sparse matrix
print("Length of M1:")
print(len(m1), "\n")

# Convert the sparse matrix to hash
print("Hash of M1:")
print(hash(m1), "\n")

# Cast to bool
print("Bool of M1:")
print(bool(m1), "\n")

# Convert a sparse matrix to a normal matrix
print("Convert M1 to a normal matrix:")
print(m1.to_matrix(), "\n")

# Delete an element from the sparse matrix
print("Delete M1[0, 0]:")
del m1[0, 0]
del m1[0, 1]
del m1[1, 1]
print(m1)

# Conovert a nXn matrix to a sparse matrix
matrix = [
  [0, 0, 1, 3],
  [0, 0, 0, 0],
  [1, 0, 0, 1],
  [0, 4, 2, 0]
]
m5 = sm.SparseMatrix.from_matrix(matrix)
print("Sparse Matrix from Matrix:")
print(m5)
```
