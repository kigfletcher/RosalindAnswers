#n, k = map(int, input().split())
n = 34
k = 2

F = [0] * (n+1)

F[1] = 1
F[2] = 1

for month in range(3, n + 1):
    F[month] = F[month-1] + k * F[month-2]

print(F[n])