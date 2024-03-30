def knapsack(bag_capacity, weights, fighting_powers, num_gadgets):
    dp_array = [[0 for _ in range(bag_capacity + 1)] for _ in range(num_gadgets + 1)]
    
    for i in range(1, num_gadgets + 1):
        for j in range(1, bag_capacity + 1):
            if weights[i - 1] > j:
                dp_array[i][j] = dp_array[i - 1][j]
            else:
                dp_array[i][j] = max(dp_array[i - 1][j], fighting_powers[i - 1] + dp_array[i - 1][j - weights[i - 1]])
                
    return dp_array[num_gadgets][bag_capacity]

for i in range(int(input())):
    bag_capacity, num_gadgets = map(int, input().split())
    
    weights = []
    fighting_powers = []
    
    for j in range(num_gadgets):
        weight, fighting_power = map(int, input().split())
        weights.append(weight)
        fighting_powers.append(fighting_power)
        
    print(knapsack(bag_capacity, weights, fighting_powers, num_gadgets))