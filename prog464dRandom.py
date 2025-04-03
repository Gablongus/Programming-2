from random import randint
import numpy as np
# import numpy as np (have to do 'pip install numpy' in the terminal)

def print_matrix(mat):
    for row in mat:
        for num in row:
            print(f"{num:3d} ", end="")
        print()


def transpose(mat):
    np_mat = np.array(mat)
    return np_mat.T  #Thats easier

# def transpose(mat):
#     rows = len(mat)
#     cols = len(mat[0])
#     transposed = [[0 for _ in range(rows)] for _ in range(cols)]
#     for i in range(rows):
#         for j in range(cols):
#             transposed[j][i] = mat[i][j]
#     return transposed


def main():
    mat1 = []
    for r in range(5):
        row1 = []
        row2 = []
        for c in range(5):
            row1.append(randint(-50, 99))
            row2.append(randint(-50, 99))
        mat1.append(row1)
    print("Matrix:")
    print_matrix(mat1)


    transposed = transpose(mat1)
    print("Transposed Matrix:")
    print_matrix(transposed)

    # mat_max = max_matrices(mat1, mat2)
    # print("\nLargest Elements:")
    # print_matrix(mat_max)

if __name__ == "__main__":
    main()