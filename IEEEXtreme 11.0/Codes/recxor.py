import math

# To solve this problem, we should know some properties of the XOR operation.
# a ^ a = 0
# a ^ 0 = a
# Therefore, to find the XOR of a range of numbers, we can use the following formula:
# xor(a,...,b) = xor(0,...,b) ^ xor(0,...,a-1) 

# The following function calculates the XOR of a range of numbers from 0 to n.
def xor(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    if n % 4 == 3:
        return 0
    
for i in range(int(input())):
    l, h, n, d1, d2 = map(int, input().split())
    
    # First we have to calculate the XOR of the values in the original rectangle.
    number_range = l*h
    
    full_xor = xor(n + number_range - 1) ^ xor(n - 1)
    
    # Before we start calculating the XOR of the inner rectangle, we have to find the top left corner of the inner rectangle.
    # We can do it in the following way.
    
    # Understand why the parameters are counted this way.
    d1_row = math.ceil((d1 - n + 1) / l) 
    d1_col = d1 - n +1 - (d1_row - 1) * l
    d2_row = math.ceil((d2 - n + 1) / l)
    d2_col = d2 - n + 1 - (d2_row - 1) * l
    
    inner_l = abs(d2_col - d1_col) + 1
    inner_h = abs(d2_row - d1_row) + 1
    
    if d1_col < d2_col:
        upper_left = d1
    else:
        upper_left = d1 - inner_l + 1
        
    # Now we can calculate the XOR of the values in the inner rectangle.
    # We can do it row by row.
    inner_xor = 0
    left_of_current_row = upper_left
    
    for i in range(inner_h):
        inner_xor ^= xor(left_of_current_row + inner_l - 1) ^ xor(left_of_current_row - 1)
        left_of_current_row += l  
        
    outer_xor = full_xor ^ inner_xor
    
    print(outer_xor)   