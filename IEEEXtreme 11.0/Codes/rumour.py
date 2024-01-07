# To get 100% points, you have to use Pypy3 instead of Python3.
# Otherwise, you will get only 80% points.

def lowest_common_ancestor(a,b):
    if a == 1:
        return 1
    else:
        numbers = []
        while b > 0 and b != a:
            b //= 2
            numbers.append(b)
        while a not in numbers:
            a //= 2
        return a


for i in range(int(input())):
    a, b = map(int,input().split())
    
    if a == b:
        print("0")
    else:
        minimum = min(a,b)
        maximum = max(a,b)
        
        lca = lowest_common_ancestor(minimum, maximum)
        
        print(len(bin(a)) + len(bin(b)) - 2*len(bin(lca)))