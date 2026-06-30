import numpy as np

# Input first matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter elements of Matrix A:")
A = []

for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("\nEnter elements of Matrix B:")
B = []

for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

print("\n========== MATRIX OPERATIONS ==========")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose of Matrix A")
print("5. Transpose of Matrix B")
print("6. Determinant of Matrix A")
print("7. Determinant of Matrix B")

choice = int(input("\nEnter your choice (1-7): "))

if choice == 1:
    print("\nAddition Result:")
    print(A + B)

elif choice == 2:
    print("\nSubtraction Result:")
    print(A - B)

elif choice == 3:
    print("\nMultiplication Result:")
    print(np.dot(A, B))

elif choice == 4:
    print("\nTranspose of Matrix A:")
    print(A.T)

elif choice == 5:
    print("\nTranspose of Matrix B:")
    print(B.T)

elif choice == 6:
    print("\nDeterminant of Matrix A:")
    print(np.linalg.det(A))

elif choice == 7:
    print("\nDeterminant of Matrix B:")
    print(np.linalg.det(B))

else:
    print("Invalid Choice!")
