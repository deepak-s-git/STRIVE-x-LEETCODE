m = len(matrix)
n = len(matrix[0])

row_has_zero = False
col_has_zero = False

#ITERATE THROUGH MATRIX TO MARK THE ZERO ROWS OR COLUMNS
for row in range(m):
    for col in range(n):
        if matrix[row][col] == 0:
            if row == 0:
                row_has_zero = True
            if col == 0:
                 col_has_zero = True
            matrix[row][0] = matrix[0][col] = 0

#ITERATE THROUGH THE MATRIX AGAIN TO UPDATE THE CELL TO BE ZERO IF ITS A ZERO ROW OR COLUMN
for row in range(1,m):
    for col in range(1,n):
        matrix[row][col] = 0 if matrix[row][0] == 0 or matrix[0][col] == 0 else matrix[row][col]

#UPDATE THE FIRST ROW AND COLUMN IF THEY ARE ZERO
if row_has_zero:
    for col in range(n):
        matrix[0][col] = 0

if col_has_zero:
    for row in range(m):
        matrix[row][0] = 0