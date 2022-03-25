class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        res = ''
        for i in self.matrix_data:
            for j in i:
                res += f'{j:>5}'
            res += '\n'
        return res

    def __add__(self, other):
        matrix_sum = []
        for i, j in enumerate(self.matrix_data):
            matrix_sum.append([])
            for m, n in enumerate(j):
                matrix_sum[i].append(self.matrix_data[i][m] + other.matrix_data[i][m])
        return Matrix(matrix_sum)


mat1 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
mat2 = Matrix([[5, 32, 3], [6, 2, 4], [1, -64, 8]])
print(mat1)
print(mat2)
mat3 = mat1 + mat2
print(mat3)
