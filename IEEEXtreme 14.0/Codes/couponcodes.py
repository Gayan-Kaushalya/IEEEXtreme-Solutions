# Performance: O(N)

# defaultdic in Python is very similar to map in C++.
from collections import defaultdict

coupons = defaultdict(int)

count = 0

for i in range(int(input())):
    code = ''.join(input().split('-'))
    
    for j in range(12):
        current = list(code)
        current[j] = '!'
        current_with_wildcard = ''.join(current)
        
        '''
        What we want is the number of pairs, not the number of codes.
        Therefore, the following method works.
        '''    
        
        count += coupons[current_with_wildcard]            
        coupons[current_with_wildcard] += 1
        
print(count)
