import math

n, black_price , pink_price = map(int, input().split())

black_total = 0
pink_total = 0

for i in range(n):
    black_amount, pink_amount = map(int, input().split())
    black_total += black_amount
    pink_total += pink_amount
    
# Using integer division gave a wrong answer
print((math.ceil(black_total/10)*black_price) + (math.ceil(pink_total/10)*pink_price))