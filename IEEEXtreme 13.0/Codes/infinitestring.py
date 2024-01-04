# The logic is bit hard to understand. I have to think about it again.
# I got the solution from the internet.

# 97 is the ASCII value of 'a'

for i in range(int(input())):
    b, x = map(int, input().split())
    
    if b == 1:
        print("a")
    elif x < b:
        print(chr(97 + x))
    else:
        j = 1
        k = 1
        
        while True:
            j *= b
            
            if j*k > x:
                break
            x -= j*k
            k += 1
            
        order = x // k
        j //= b
        count = x%k
        
        while True:
            if count == 0:
                print(chr(97 + order//j))
                break
            order %= j
            j //= b
            count -= 1