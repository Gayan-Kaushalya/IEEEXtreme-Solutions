# To pass all the test cases, you should use Pypy3 instead of Python3.
# I got the solution from the internet.
import math

mod = 10**9 + 7

n = int(input())

max_height = math.floor(math.log2(n)) + 1

pascal = [0]*(max_height)
pascal[0] = 1

total = 0

h = 1
row_total = 1

while h <= max_height:
    if h > 1:
        for i in range(h - 1, 0, -1):
            pascal[i] += pascal[i - 1]
            
    x = n - row_total
    
    counts = [0] * (x + 1)
    counts[0] = 1
    
    for i in range(h):
        p = pascal[i]
        
        for j in range(x - p + 1):
            counts[j + p] += counts[j]
            counts[j + p] %= mod
            
    total += counts[x]
    total %= mod
    
    h += 1
    row_total *= 2
    
print(total) 