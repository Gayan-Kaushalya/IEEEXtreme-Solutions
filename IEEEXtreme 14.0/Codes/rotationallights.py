# The logic is bit hard to understand. I found the solution on the internet.

'''
The steps are as follows:
1. Create an array of the switched on lights and calculate the distance between adjacent pairs of lights. 
2. Our goal is to find how often that pattern repeats. Then the answer is (total number of lights // total number of repetitions) - 1.
3. To find the total number of repetitions, we must rotate a copied version of distance array that is in a deque and compare it with the original until a match is found.
'''

from collections import deque

N, T = map(int, input().split())
switched_on = list(map(int, input().split()))

distances = [switched_on[i] - switched_on[i - 1] for i in range(1, N)]

distances.append(T - switched_on[-1] + switched_on[0]) # distance between the last and the first light

distances_copy = deque(distances)

for i in range(1, T + 1):
    distances_copy.rotate()
    
    for a,b in zip(distances, distances_copy):
        if a != b:
            break
    else:
        repetitions = N // i
        print((T // repetitions) - 1)
        break  