# To pass all test cases, you must use Pypy3 instead of Python 3.

mod = 1000000007
max = 10**6

f = [0] * (max + 1)
f[0] = 1

for i in range(1, max + 1):
    j = 2
    
    while j - 1 <= i:
        f[i] += f[i - j + 1]
        f[i] %= mod
        j *= 2
        
for i in range(1, max + 1):
    f[i] *= 2
    f[i] %= mod
    
s = [0] * (max + 1)
s[0] = f[0]

for i in range(1, max + 1):
    s[i] = s[i - 1] + f[i]
    s[i] %= mod
    
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    
    if a != 0:
        print((s[b] - s[a - 1] + mod) % mod)
    else:
        print((s[b] + mod) % mod)