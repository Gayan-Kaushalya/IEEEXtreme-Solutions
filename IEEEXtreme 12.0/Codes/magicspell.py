translations = {"xrto": "0", "pmr": "1", "yep": "2", "yjtrr": "3", "gpit": "4", "gobr": "5", "doc": "6", "drbrm": "7", "rohjy": "8", "momr": "9"}

result = 1
numbers = []

for tests in range(int(input())):
    x = input().split()
    
    number = ""
    
    for word in x:
        number += translations[word]
        
    numbers.append(number)
    
for number in numbers:
    result *= int(number,16)
    
print(result)