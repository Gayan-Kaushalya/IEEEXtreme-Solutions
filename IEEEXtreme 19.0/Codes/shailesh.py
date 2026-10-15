# Should use PyPy3 to get full marks.
for _ in range(int(input())):
    n = int(input())

    # Odd numbers and powers of two have no solution
    if n % 2 == 1 or (n & (n - 1)) == 0:
        print(-1)
        continue

    found = False

    # Try toggling each bit of n
    for i in range(64):
        a = n ^ (1 << i)

        # We need b + c = 2*n - a
        # and b ^ c = n ^ a
        s = 2 * n - a
        d = n ^ a

        if s < d:
            continue

        b = (s - d) // 2
        c = b + d

        # Ensure b and c have XOR d
        if b <= 0 or (b & d) != 0:
            continue

        # All three integers must be distinct
        if len({a, b, c}) != 3:
            continue

        print(a, b, c)
        found = True
        break

    if not found:
        print(-1)
