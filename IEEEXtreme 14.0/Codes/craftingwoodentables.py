# The logic is bit hard to understand. I have to think about it again.
# I got the solution from the internet.

import math

'''
Crafting a wooden table requires C pieces of wood. 
Pocket has N slots, and each slot can hold either a single wooden table, or a pile of wood with at most P pieces of wood.
Currently there are W pieces of wood. 
'''

c, n, p, w = list(map(int, input().split()))

answer = 0

low = 0
high = min (n, w // c)

while low <= high:
    tables = (low + high) // 2
    req_wood = tables * c
    wood_left = w - req_wood
    pockets_needed = math.ceil((wood_left/p))
    if pockets_needed <= n - tables:
        answer = tables
        low = tables + 1
    else:
        high = tables - 1
        
print(answer)