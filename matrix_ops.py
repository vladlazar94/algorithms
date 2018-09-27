def rotate_matrix(matrix):
    """ Rotates an NxN matrix by 90 degrees. """
    def transform(ln, col):
        return col, len(matrix) - ln - 1

    for line in range(0, int(len(matrix) / 2)):
        for column in range(line, len(matrix) - line - 1):
            
            curr_elem = matrix[line][column]
            curr_line = line
            curr_col = column

            for _ in range(0, 4):

                next_line = transform(curr_line, curr_col)[0]
                next_col = transform(curr_line, curr_col)[1]

                temp_val = matrix[next_line][next_col]
                matrix[next_line][next_col] = curr_elem
                curr_elem = temp_val

                curr_line = next_line
                curr_col = next_col


def zero_element(matrix):
    """ If an element in the given matrix is 0, then
        its entire row and column will be set to 0. """
    row_bools = [False for x in range(len(matrix))]
    col_bools = [False for x in range(len(matrix))]

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == 0:
                row_bools[row] = True
                col_bools[column] = True

    for rowIndex in range(len(row_bools)):
        if row_bools[rowIndex]:
            for columnIndex in range(len(matrix)):
                matrix[rowIndex][columnIndex] = 0

    for columnIndex in range(len(col_bools)):
        if col_bools[columnIndex]:
            for rowIndex in range(len(matrix)):
                matrix[rowIndex][columnIndex] = 0