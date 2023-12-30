for x in range(int(input())):
    m, n, k = map(int, input().split())
    
    rooms = []
    
    for i in range(m):
        rooms.append(int(input()))
        
    rooms.sort()
    
    for i in range(k):
        rooms[i] = n - rooms[i]
        
    print(sum(rooms))