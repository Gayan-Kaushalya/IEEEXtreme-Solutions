n, k, l = map(int, input().split())

square_area = 4 * l * l

total_area = square_area

if k >= 2 * l:
    extra_area = square_area
else:
    extra_area = 4 * l * l - (2 * l - k) * (2 * l - k)

total_area += extra_area * (n - 1)

print(total_area)