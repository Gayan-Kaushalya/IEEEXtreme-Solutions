for i in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    
    numbers.sort()
    
    left_stack = []
    right_stack = []
    
    for x in numbers:
        if x == 0:
            left_stack.append(x)
            continue
        
        if len(left_stack) == 0 or left_stack[-1] == 0:
            left_stack.append(x)
        elif len(right_stack) == 0:
            right_stack.append(x)
        else:
            if left_stack[-1] > right_stack[-1]:
                right_stack.append(x)
            else:
                left_stack.append(x)
    
    left_stack.extend(right_stack[::-1])
    print(sum(left_stack[i] * left_stack[i + 1] for i in range(len(left_stack) - 1)))
    print(*left_stack)