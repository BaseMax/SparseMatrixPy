import os
import SparseMatrix as sm

# Create main function
def main():
    print("Hello World")
    print("The current working directory is {0}".format(os.getcwd()))

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

# This is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    main()
