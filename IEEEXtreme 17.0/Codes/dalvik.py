# This answer was created with the help of ChatGPT.
from math import gcd

def solve(A, B, C):
    g = gcd(A, B)
    p = A // g
    q = B // g

    if q <= C:
        return q

    p0, q0 = 0, 1
    p1, q1 = 1, 0

    while q != 0:
        a = p // q
        p2 = a * p1 + p0
        q2 = a * q1 + q0

        if q2 > C:
            k = (C - q0) // q1

            pn = p0 + k * p1
            qn = q0 + k * q1

            e1 = abs(A * q1 - B * p1)
            e2 = abs(A * qn - B * pn)

            left = e1 * qn
            right = e2 * q1

            if left < right:
                return q1
            elif right < left:
                return qn
            else:
                return min(q1, qn)

        p0, q0 = p1, q1
        p1, q1 = p2, q2
        p, q = q, p % q

    return q1


T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    print(solve(A, B, C))
