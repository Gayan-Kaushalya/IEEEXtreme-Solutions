import math

n, m, s = map(int, input().split())

# This is very similar to binary search.
# Worst case happens when the last pump is the broken one.
# Then total time to repair is log2(n - 1) * s
# Total time to travel is (n - 1) * m

# If the pump in working properly, we go downhill. Otherwise, we go uphill.

print(math.ceil(math.log2(n - 1)) * s + (n - 1) * m)