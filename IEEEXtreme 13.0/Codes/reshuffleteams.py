combinations = [('A', 'B', 'C', 'D'), ('A', 'B', 'D', 'C'), ('A', 'C', 'B', 'D'), ('A', 'C', 'D', 'B'), ('A', 'D', 'C', 'B'), ('A', 'D', 'B', 'C')]

for i in range(int(input())):
    current_sitting = input()
    
    a = current_sitting.count('A')
    b = current_sitting.count('B')
    c = current_sitting.count('C')
    d = current_sitting.count('D')
    
    counts = {'A': a, 'B': b, 'C': c, 'D': d}
    
    round_sitting = current_sitting * 3
    letters = ['A', 'B', 'C', 'D']
    
    result = 10**5
    
    for combination in combinations:
        offset = 0
        bad = []
        
        for letter in combination:
            current = round_sitting[offset : offset + counts[letter]]
            bad.append(len(current) - current.count(letter))
            offset += counts[letter]
            
        result = min(sum(bad), result)
        
        for x in range(1, (len(current_sitting) + 1)):
            offset = x
            wrong = []
            
            for index, letter in enumerate(combination):
                if counts[letter] == 0:
                    wrong.append(0)
                    continue
                
                new_bad = bad[index]
                
                if round_sitting[offset - 1] == letter:
                    new_bad += 1
                if round_sitting[offset + counts[letter] - 1] == letter:
                    new_bad -= 1
                    
                wrong.append(new_bad)
                offset += counts[letter]
                
            if result > sum(wrong):
                result = sum(wrong)
                
            bad = wrong
            
    print(result)