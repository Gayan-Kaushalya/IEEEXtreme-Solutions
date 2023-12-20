import math

w, h, a, b, m, c = map(int, input().split())

number_of_tiles = math.ceil(w/a) * math.ceil(h/b)
price_of_tiles = math.ceil(number_of_tiles/10) * m

inches_to_cut = 0

if w%a:
    inches_to_cut += b
    
if h%b:
    inches_to_cut += a
    
price_of_cut = inches_to_cut * c

print(price_of_tiles)
print(price_of_cut)

print(price_of_tiles + price_of_cut)