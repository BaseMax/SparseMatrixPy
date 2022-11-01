import SparseMatrix as sm

# Create main function
def main():
    print("Hello World")

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
    print(len(m1))

    # Convert the sparse matrix to hash
    print("Hash of M1:")
    print(hash(m1))

    # Cast to bool
    print("Bool of M1:")
    print(bool(m1))

    # Delete an element from the sparse matrix
    print("Delete M1[0, 0]:")
    del m1[0, 0]
    print(m1)
    

# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    # Call the main function
    main()
