#코드 길이:456 byte(s) / 수행 시간:14 ms / 메모리 :14316 kb
import sys
d=[[0]*20 for _ in range(20)]

for i in range(19) :
  a = list(map(int, sys.stdin.readline().rstrip().split()))
  for j in range(19) :
    d[i+1][j+1] = a[j]

n = int(sys.stdin.readline().rstrip())
for _ in range(n) :
  x,y=map(int,sys.stdin.readline().rstrip().split())
  for i in range(1, 20) :
    d[i][y] ^= 1  # y열의 상태를 뒤집음
    d[x][i] ^= 1  # x행의 상태를 뒤집음

for row in d[1:]:
  print(*row[1:])
