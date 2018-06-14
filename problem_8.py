# Problem_8: Write an algorihm such that if an element in a NxN matrix is 0, 
# then its entire row and column is set to 0.

# O(n^2) where n is the size of the matrix.
# Expects a row-major square matrix.
def zeroElement(matrix):
    
    rowBools = [False for x in range(len(matrix))]
    columnBools =  [False for x in range(len(matrix))]

    for row in range (len(matrix)):
        for column in range(len(matrix)):
            if matrix[row][column] == 0:     
                rowBools[row] = True
                columnBools[column] = True

    for rowIndex in range (len(rowBools)):      
        if rowBools[rowIndex] == True:
            for columnIndex in range(len(matrix)):
                matrix[rowIndex][columnIndex] = 0

    for columnIndex in range (len(columnBools)):
        if columnBools[columnIndex] == True:
            for rowIndex in range(len(matrix)):
                matrix[rowIndex][columnIndex] = 0


    