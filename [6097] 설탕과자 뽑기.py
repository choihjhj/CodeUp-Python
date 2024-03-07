#코드 길이:551 byte(s) / 수행 시간:12 ms / 메모리 :14448 kb
import sys

h, w = map(int, sys.stdin.readline().rstrip().split())
result = [[0] * (w + 1) for _ in range(h + 1)]
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    l, d, x, y = map(int, sys.stdin.readline().rstrip().split())
    if d == 1:  # 세로방향
        for i in range(x, x + l):
            result[i][y] = 1
    elif d == 0:  # 가로방향
        for i in range(y, y + l):
            result[x][i] = 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(result[i][j], end=' ')
    print()
