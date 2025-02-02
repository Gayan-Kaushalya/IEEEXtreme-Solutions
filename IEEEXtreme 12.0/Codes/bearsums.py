for x in range (int(input())):
    s, e = map(int, input().split())
    numbers = list(map(int, input().split()))

    seen = set()
    solution = None
    
    for number in numbers:
        if (s - number) in seen:
            solution = [s - number, number]
            solution.sort()
            break
        else:
            seen.add(number)
            
    if solution:
        print(*solution)
    else:
        print("!OK")           