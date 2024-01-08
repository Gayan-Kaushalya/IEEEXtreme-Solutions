for i in range(int(input())):
    a, b = map(int,input().split())
    
    answer = 0
    
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
        answer += 1
        
    print(answer)