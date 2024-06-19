# I got the solution from the internet. 
n, m, k = map(int, input().split())

x_limit = n + m + 5
y_limit = n + m + 5

matrix = [[0 for i in range(y_limit)] for j in range(x_limit)]
lions = []

for i in range(k):
    x, y, d = map(int, input().split())

    # https://math.stackexchange.com/questions/732679/how-to-rotate-a-matrix-by-45-degrees
    rotated_x = x + y + 1
    rotated_y = y - x + n
    lions.append((rotated_x, rotated_y, d))
    
    matrix[max(rotated_x - d, 0)][max(rotated_y - d, 0)] += 1
    
    if rotated_y + d + 1 < y_limit:
        matrix[max(rotated_x - d, 0)][rotated_y + d + 1] -= 1
    
    if rotated_x + d + 1 < x_limit:
        matrix[rotated_x + d + 1][max(rotated_y - d, 0)] -= 1
        
    if rotated_x + d + 1 < x_limit and rotated_y + d + 1 < y_limit:
        matrix[rotated_x + d + 1][rotated_y + d + 1] += 1
        
for j in range(1, y_limit):
    matrix[0][j] += matrix[0][j - 1]
    
for i in range(1, x_limit):
    matrix[i][0] += matrix[i - 1][0]
    
    for j in range(1, y_limit):
        matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]

max_num_of_lions = 0
index = 0

for i, (x, y, d) in enumerate(lions):
    if matrix[x][y] > max_num_of_lions:
        max_num_of_lions = matrix[x][y]
        index = i
        
print(index + 1, max_num_of_lions - 1)   

# We add 1 to the index because the index starts from 0.
# We subtract 1 from the max_num_of_lions because we are counting the lion that is already there.