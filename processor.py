import copy
import math


def menu(choose):
    if choose == 1:
        print('''
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    elif choose == 2:
        print('''
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
    return input('Your choice: ')


def dimension(num):
    x = []
    if num == 1:
        y = input('Enter size of first matrix: ')
    elif num == 2:
        y = input('Enter size of second matrix: ')
    elif num == 3:
        y = input('Enter size of matrix: ')
    else:
        y = input('Enter matrix size: ')
    y = y.split()
    for i in range(2):
        x.append(int(y[i]))
    return x


def matrix(row, column, num):
    if num == 1:
        print('Enter first matrix:')
    elif num == 2:
        print('Enter second matrix: ')
    else:
        print('Enter matrix:')
    x = []
    for i in range(row):
        y = input()
        y = y.split()
        z = []
        for j in range(column):
            z.append(float(y[j]))
        x.append(z)
    return x


def print_matrix(matrix_, row, column, choice='no'):
    checker = 0
    for x in range(row):
        for y in range(column):
            if not matrix_[x][y].is_integer():
                checker = 1
    for x in range(row):
        for y in range(column):
            if checker == 0:
                matrix_[x][y] = str(int(matrix_[x][y]))
            elif choice == 'yes':  # round up
                frac, whole = math.modf(matrix_[x][y])
                if matrix_[x][y] == 0.0 or matrix_ == -0.0:
                    matrix_[x][y] = '0'
                elif frac == 0:
                    matrix_[x][y] = str(int(whole))
                else:
                    dot = str(frac).find('.')
                    matrix_[x][y] = str(whole + float(str(frac)[:dot+3]))
            elif choice == 'no':
                matrix_[x][y] = str(matrix_[x][y])
    for i in range(row):
        temp = ' '.join(matrix_[i])
        print(temp)


def addition(matrix_one, matrix_two, row, column):
    sum_matrix = []
    for i in range(row):
        c = []
        for j in range(column):
            c.append(float(matrix_one[i][j] + matrix_two[i][j]))
        sum_matrix.append(c)
    print_matrix(sum_matrix, row, column)


def multiply_constant(_matrix, multiply, row, column, choice='no'):
    answer = []
    for a in range(row):
        d = []
        for b in range(column):
            d.append(float(_matrix[a][b] * multiply))
        answer.append(d)
    if choice == 'no':
        print_matrix(answer, row, column, 'no')
    else:
        print_matrix(answer, row, column, 'yes')


def multiply_matrix(matrix1, matrix2, matrix1_r, matrix1_c, matrix2_r, matrix2_c):
    if matrix1_c != matrix2_r:
        print('The operation cannot be performed.')
    else:
        answer = []
        for i in range(matrix1_r):
            c = []
            for j in range(matrix2_c):
                total = 0
                for a in range(matrix1_c):
                    total += (matrix1[i][a] * matrix2[a][j])
                c.append(float(total))
            answer.append(c)
        print_matrix(answer, matrix1_r, matrix2_c)


def transpose(_matrix, row, column, select):
    copy_ = copy.deepcopy(_matrix)
    for i in range(row):
        for j in range(column):
            if select == '1':
                _matrix[j][i] = copy_[i][j]
            elif select == '2':
                _matrix[i][j] = copy_[column - j - 1][row - i - 1]
            elif select == '3':
                _matrix[i][j] = copy_[i][column - j - 1]
            else:
                _matrix[i][j] = copy_[row - i - 1][j]
    return _matrix


def determinant(_matrix, layer):
    result = 0
    if layer == 1:
        return _matrix[0][0]
    elif layer == 2:
        return _matrix[0][0] * _matrix[1][1] - _matrix[0][1] * _matrix[1][0]
    else:
        for x in range(layer):
            small_matrix = []
            for i in range(layer):
                if i == 0:
                    continue
                small_row = []
                for j in range(layer):
                    if j == x:
                        continue
                    else:
                        small_row.append(_matrix[i][j])
                small_matrix.append(small_row)
            result += (-1) ** x * _matrix[0][x] * determinant(small_matrix, layer - 1)
        return result


def inverse(_matrix, row, column):
    checker = 0
    det = determinant(_matrix, row)
    if det == 0:
        checker = 1
    else:
        det = 1 / det
    copy_matrix = copy.deepcopy(_matrix)
    i = 0
    j = 0
    small_matrix = []
    while i != row and j != column:
        for x in range(row):
            small_row = []
            if x == i:
                continue
            for y in range(column):
                if y == j:
                    continue
                else:
                    small_row.append(_matrix[x][y])
            small_matrix.append(small_row)
            small_row = []
        copy_matrix[i][j] = (-1) ** (i + j) * determinant(small_matrix, row - 1)
        small_matrix = []
        j += 1
        if j == column:
            i += 1
            j = 0
    if checker == 1:
        print("This matrix doesn't have an inverse")
    else:
        cofactor = transpose(copy_matrix, row, column, '1')
        multiply_constant(cofactor, det, row, column, 'yes')


choice = menu(1)
while choice != '0':
    if choice == '1':
        dimension_1 = dimension(1)
        matrix_1 = matrix(dimension_1[0], dimension_1[1], 1)
        dimension_2 = dimension(2)
        matrix_2 = matrix(dimension_2[0], dimension_2[1], 2)
        if dimension_1 != dimension_2:
            print('The operation cannot be performed.')
        else:
            print('The result is:')
            addition(matrix_1, matrix_2, dimension_1[0], dimension_1[1])
        choice = menu(1)
    elif choice == '2':
        dimension_3 = dimension(3)
        matrix_3 = matrix(dimension_3[0], dimension_3[1], 3)
        constant = float(input('Enter constant: '))
        print('The result is:')
        multiply_constant(matrix_3, constant, dimension_3[0], dimension_3[1])
        choice = menu(1)
    elif choice == '3':
        dimension_1 = dimension(1)
        matrix_1 = matrix(dimension_1[0], dimension_1[1], 1)
        dimension_2 = dimension(2)
        matrix_2 = matrix(dimension_2[0], dimension_2[1], 2)
        print('The result is:')
        multiply_matrix(matrix_1, matrix_2, dimension_1[0], dimension_1[1], dimension_2[0], dimension_2[1])
        choice = menu(1)
    elif choice == '4':
        choice1 = menu(2)
        dimension_1 = dimension(3)
        matrix_1 = matrix(dimension_1[0], dimension_1[1], 1)
        print('The result is:')
        print_matrix(transpose(matrix_1, dimension_1[0], dimension_1[1], choice1), dimension_1[0], dimension_1[1])
        choice = menu(1)
    elif choice == '5':
        dimension_ = dimension(4)
        matrix_ = matrix(dimension_[0], dimension_[1], 3)
        print('The result is:')
        print(determinant(matrix_, dimension_[0]))
        choice = menu(1)
    elif choice == '6':
        dimension_ = dimension(4)
        matrix_ = matrix(dimension_[0], dimension_[1], 3)
        inverse(matrix_, dimension_[0], dimension_[1])
        choice = menu(1)
