rows, columns = [int(x) for x in input().split(", ")]
matrix = []
matrix_sum = 0

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
    matrix_sum += sum(matrix[row])

print(matrix_sum)
print(matrix)