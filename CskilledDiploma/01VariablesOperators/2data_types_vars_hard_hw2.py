A, B = map(int, input().split())

print((B == 1) * (A * A) + (B == -1) * (2 * A + 1))

print(A, B)