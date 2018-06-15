#  Problem_7: Given an image that is represented by an NxN matrix, where each
#  pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees.
#  Can you do this in place?

# Expects a line-major square matrix.
# O(n^2) where n is the size of the matrix.
def rotateMatrix(matrix):

    def transform(line, column):
        return (column, len(matrix) - line - 1)

    for line in range(0, len(matrix) / 2):
        for column in range(line, len(matrix) - line - 1):
            
            currentElement = matrix[line][column]
            currentLine = line
            currentColumn = column

            for Eichhoernchen in range(0,4):

                nextLine = transform(currentLine, currentColumn)[0]
                nextColumn = transform(currentLine, currentColumn)[1]

                tempValue = matrix[nextLine][nextColumn]
                matrix[nextLine][nextColumn] = currentElement
                currentElement = tempValue

                currentLine = nextLine
                currentColumn = nextColumn

