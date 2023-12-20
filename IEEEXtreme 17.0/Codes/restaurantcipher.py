for x in range(int(input())):
    times = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0}
    letters = list(times.keys())
     
    code = input()
    for x in code:
        if x in times:
            times[x] += 1
    
    values = list(times.values())
    
    print(letters[values.index(max(values))].capitalize())  
         