#코드 길이:525 byte(s) / 수행 시간:10 ms / 메모리 :14316 kb
import sys

d = [[0] * 11 for _ in range(11)]

for i in range(10):
    s = sys.stdin.readline().rstrip().split()
    for j in range(10):
        d[i + 1][j + 1] = int(s[j])

x, y = 2, 2
while True :
  if d[x][y] == 0 : d[x][y] = 9
  elif d[x][y] == 2 :
    d[x][y] = 9
    break

  if (d[x][y+1]==1 and d[x+1][y]==1) or (x==9 and y==9) : break

  if d[x][y+1] != 1 : y += 1
  elif d[x+1][y] != 1 : x += 1


for i in range(1, 11):
    for j in range(1, 11):
        print(d[i][j], end=' ')
    print()
