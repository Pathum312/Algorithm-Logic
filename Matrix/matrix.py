"""
Description:
    Matrix or Grid is a two-dimensional array mostly used in mathematical and scientific calculations. 
    It is also considered as an array of arrays, where array at each index has the same size.
"""

print("\n### Declaring a Matrix ###\n")

rows: int = 3
cols: int = 3

print(f"rows: {rows}\ncols: {cols}\n")

matrix: list[list[int]] = [[0] * cols] * rows

print(f"1. Initial Matrix: {matrix}\n\n")


print("### Accessing Elements of a Matrix ###\n")

second_matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(f"Matrix: {second_matrix}\n")

print(f"1. First element of first row: {second_matrix[0][0]}\n")
print(f"2. Third element of second row: {second_matrix[1][2]}\n")
print(f"3. Second element of third row: {second_matrix[2][1]}\n\n")


print("### Traversing a Matrix ###\n")

print(f"Matrix: {second_matrix}\n")


def print_matrix(matrix: list[list[int]]) -> None:
    """
    Prints the elements of a matrix in row-major order.

    Parameters:
        matrix (list[list[int]]): The matrix to be printed.

    Returns:
        None
    """
    for row in matrix:
        for value in row:
            print(value, end=" ")

        print()

    print("\n")


print_matrix(matrix=second_matrix)


print("### Searching in a Matrix ###\n")
