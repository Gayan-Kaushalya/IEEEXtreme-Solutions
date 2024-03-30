num_players = int(input())

performances_indices = list(map(int, input().split()))

for i in range(int(input())):
    expected_index = int(input())
    
    potential_players = []
    
    # If a player has 1 for a skill and the team has 0 for it, we have to exclude that player.
    for index in performances_indices:
        if index & expected_index == index:
            potential_players.append(index)
            
    team_performance_index = 0
    
    for player in potential_players:
        team_performance_index |= player
        
    if team_performance_index == expected_index:
        print("YES")
    else:
        print("NO")