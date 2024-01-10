'''
This part had to be added to the code to pass the test cases. 

Otherwise it gives the following error:
    ValueError: Exceeds the limit (4300) for integer string conversion: value has 5432 digits.
'''

import sys
sys.set_int_max_str_digits(0)

fib = {2: 2, 1: 1}
numbers = []

y = int(input())

for j in range(y):
    x = int(input())
    numbers.append(x)
    for i in range(3, x + 1):
        if i not in fib:
            fib[i] = fib[i - 1] + fib[i - 2]
for i in numbers:
    print(fib[i])