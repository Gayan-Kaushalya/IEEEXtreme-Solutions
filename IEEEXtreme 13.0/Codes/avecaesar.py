phrases = []
result = []

for i in range (int(input())):
    phrases.append(input())
    
for phrase in phrases:
    substrings = []
    
    start = 0
    
    for i in range(1,len(phrase)):
        if phrase[i] < phrase[i-1]:
           substrings.append(phrase[start:i])
           start = i 
    substrings.append(phrase[start:])
    
    for j in range(1,len(substrings)):
        if substrings[j] < substrings[j-1]:
            result.append(0)
            break
    else:
        result.append(1)
  
for i in result:
    print(i,end="")      