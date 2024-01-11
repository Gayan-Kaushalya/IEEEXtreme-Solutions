fib = [1, 1, 2]

for i in  range(3, 60):
    fib.append((fib[i-1] + fib[i-2]) % 10)
    
for j in range(int(input())):
    x = int(input()) % 60
    print(fib[x])