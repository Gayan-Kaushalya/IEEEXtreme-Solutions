x = int(input())

heights = {}

for i in range(x):
    data = input().split()
    
    if int(data[1]) not in heights:
        lis = []
        lis.append(data[0])
        heights[int(data[1])] = lis
    else:
        heights[int(data[1])].append(data[0])
        
y = list(heights.keys())
y.sort()

count = 1

for k in y:
    heights[k].sort()
    for criminal in heights[k]:
        print(criminal, end = " ")
    print(count, end = " ")
    count += len(heights[k]) - 1
    print(count)
    count += 1
        