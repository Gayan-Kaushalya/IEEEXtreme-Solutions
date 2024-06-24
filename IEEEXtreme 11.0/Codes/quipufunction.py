def g(x):
  u = int(x**0.5)
  return 2*sum(x//k for k in range(1, u + 1)) - u**2 - 1

def quipu(a, b, d):
  return g(b) - g(b//d) - g(a - 1) + g((a - 1)//d)

t, a, b = map(int, input().split())

for i in range(t):
  print(quipu(a, b, int(input())))