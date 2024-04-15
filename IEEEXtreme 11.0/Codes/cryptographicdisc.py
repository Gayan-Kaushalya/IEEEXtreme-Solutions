import math

radius = int(input())

angles = {}

for i in range(26):
    letter, angle = input().split()
    angle = float(angle)
    
    # We have to get sine and cosine of the angle.
    # then we multiply by the radius to get the x and y coordinates.
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    
    angles[letter] = (x, y)
    
phrase = input()

# We have to turn all letters to uppercase and remove characters that are not letters.
phrase = ''.join([c.upper() for c in phrase if c.isalpha()])

current_position = (0, 0)
total_distance = 0

for letter in phrase:
    x, y = angles[letter]
    distance = math.sqrt((x - current_position[0])**2 + (y - current_position[1])**2)
    total_distance += distance
    current_position = (x, y)
    
print(math.ceil(total_distance))