import sys

def find(arr, i):
    if arr[i] != i:
        arr[i] = find(arr, arr[i])
    return arr[i]

def union(arr, i1, i2, j1, j2):
    arr[j1] = arr[i2]
    arr[j2] = arr[i1]

N = int(input())  
arr = list(range(2 * N))

while True:
    a, b = [int(i) - 1 for i in input().split()]

    f_a1, f_a2, f_b1, f_b2 = find(arr, 2 * a), find(arr, 2 * a + 1), find(arr, 2 * b), find(arr, 2 * b + 1)
    
    if (f_a1 == f_b1) or (f_a2 == f_b2):
        print(0)
        break
    
    union(arr, f_a1, f_a2, f_b1, f_b2)
    print(1)
    sys.stdout.flush()