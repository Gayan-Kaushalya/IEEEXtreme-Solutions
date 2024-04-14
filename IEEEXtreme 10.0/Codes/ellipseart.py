# To pass all the test cases, you must use Pypy3 instead of Python 3.
import math

def check(x, y):
    for ellipse in ellipse_parameters:
        if math.sqrt((x - ellipse[0])**2 + (y - ellipse[1])**2) + math.sqrt((x - ellipse[2])**2 + (y - ellipse[3])**2) <= ellipse[4]:
            return True
    return False

for i in range(int(input())):
    ellipse_parameters = []
    
    num_ellipses = int(input())
    
    for j in range(num_ellipses):
        x1, y1, x2, y2, r = map(int, input().split())
        ellipse_parameters.append((x1*10, y1*10, x2*10, y2*10, r*10))
        
    count = 0
    
    for x in range(-500, 500, 2):
        for y in range(-500, 500, 2):
            if not check(x, y):
                count += 1
                
    answer = round(count / 2500)
    
    print(str(answer) + "%")  