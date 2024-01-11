# The logic is bit hard to understand. I have to think about it again.
# I got the solution from the internet.

def pwr(x, q, m):
    if q == 0:
        return 1
    elif q == 1:
        return x % m
    p = pwr(x, q // 2, m)
    p = (p * p) % m
    
    if q % 2 == 1:
        p = (p * x) % m
    return p

for i in range (int(input())):
    x, y = map(int, input().split())
    mod = pwr(10, y, 10**18)          # Calculate the power of 10^y % 10^18
    
    x %= mod
    
    k = pwr(x, 10**10, mod)           # Calculate X^[4*10^(Y-1) or any multiple of it]
    
    answer = k
    
    for j in range(86400):
        k = (k * x) % mod
        answer = min(answer, k)
        
    print(answer)    