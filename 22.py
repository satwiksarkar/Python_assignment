import re

# input
n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input())

# read column-wise
decoded = ""
for col in range(m):
    for row in range(n):
        decoded += matrix[row][col]

# replace unwanted symbols
result = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded)

print(result)
