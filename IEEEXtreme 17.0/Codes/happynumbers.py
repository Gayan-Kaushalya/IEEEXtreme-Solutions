# This answer was created with the help of ChatGPT.
MAX_DIGITS = 17
MAX_SUM = 81 * MAX_DIGITS 

happy = [False] * (MAX_SUM + 1)
state = [0] * (MAX_SUM + 1)
# 0 = unvisited
# 1 = visiting
# 2 = happy
# 3 = unhappy


def next_sum(x):
    s = 0
    while x:
        d = x % 10
        s += d * d
        x //= 10
    return s


def is_happy_sum(x):
    if x == 1:
        return True

    if state[x] == 2:
        return True

    if state[x] == 3:
        return False

    if state[x] == 1:
        return False  # cycle

    state[x] = 1

    ans = is_happy_sum(next_sum(x))

    state[x] = 2 if ans else 3
    happy[x] = ans

    return ans


for s in range(1, MAX_SUM + 1):
    happy[s] = is_happy_sum(s)


def count_happy(x):
    if x < 0:
        return 0

    digits = list(map(int, str(x)))
    n = len(digits)

    memo = {}

    def dfs(pos, sqsum, tight):
        if pos == n:
            return 1 if happy[sqsum] else 0

        if not tight:
            key = (pos, sqsum)
            if key in memo:
                return memo[key]

        limit = digits[pos] if tight else 9

        ans = 0

        for d in range(limit + 1):
            ans += dfs(
                pos + 1,
                sqsum + d * d,
                tight and d == limit
            )

        if not tight:
            memo[(pos, sqsum)] = ans

        return ans

    return dfs(0, 0, True)


L, R = map(int, input().split())

print(count_happy(R) - count_happy(L - 1))
