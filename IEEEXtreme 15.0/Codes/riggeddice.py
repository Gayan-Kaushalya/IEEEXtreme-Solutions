for g in range(int(input())):
    alice_has_dice_a = True

    alice_score = 0
    bob_score = 0
    
    first_die_six_count = 0
    second_die_six_count = 0

    for r in range(int(input())):
        a, b = map(int, input().split())

        alice_score += a
        bob_score += b
        
        if alice_has_dice_a:
            if a == 6:
                first_die_six_count += 1
                
            if b == 6:
                second_die_six_count += 1
                
        else:
            if a == 6:
                second_die_six_count += 1
                
            if b == 6:
                first_die_six_count += 1
                       
        if alice_score != bob_score:
            alice_has_dice_a = not alice_has_dice_a

    if first_die_six_count > second_die_six_count:
        print(1)   
    else:
        print(2)