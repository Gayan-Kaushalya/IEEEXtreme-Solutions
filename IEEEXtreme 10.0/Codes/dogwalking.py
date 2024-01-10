# The logic is bit hard to understand. I have to think about it again.
# I got the solution from the internet.

for i in range (int(input())):
    n, k = map(int, input().split())
    dogs = []
    
    for j in range (n):
        dogs.append(int(input()))
        
    dogs.sort()
    total_range = dogs[-1] - dogs[0]
    
    differences = []
    
    for a, b in zip(dogs, dogs[1:]):
        differences.append(b - a)
        
    differences.sort()
    
    print(total_range + sum(differences[:k - 1])) 