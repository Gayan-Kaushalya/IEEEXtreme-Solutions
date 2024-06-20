mod = 500000003

factorial = [0] * 1000005
factorial[0] = 1
factorial[1] = 1

for i in range(2, 1000005):
    factorial[i] = (factorial[i-1] * i) % mod


'''
Rearranging Fermat's Little Theorem, we can get the following:
a^(p-1) = 1 (mod p)
a^(p-2) = a^(-1) (mod p)

So, we can calculate the modular multiplicative inverse of a number by raising it to the power of p-2.
'''
def modular_multiplicative_inverse(n):
    return pow(n, mod - 2, mod)
    

# This somehow works.
def nCr(a, b):
    return (factorial[a] * ((modular_multiplicative_inverse(factorial[b]) * modular_multiplicative_inverse(factorial[a-b])) % mod)) % mod


def mod_function(a, b):
    c = a - b
    d, e, f = 0,0,0
    
    for i in range(1, 40):
        d += (a >> i)
        e += (b >> i)
        f += (c >> i)
     
    if d > e + f:
        return True
    return False


def answer(a, b):
    even = mod_function(a, b)
    combinations = nCr(a, b) 
    
    if even:
        if (combinations % 2) == 1:
            return combinations + mod
        else:
            return combinations
    else:
        if (combinations % 2) == 1:
            return combinations
        else:
            return combinations + mod


for x in range(int(input())):
    a, b, c = map(int, input().split())
    print(pow(a, answer(b, c), 1000000007))