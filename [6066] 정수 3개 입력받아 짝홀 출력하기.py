#코드 길이:118 byte(s) / 수행 시간:13 ms / 메모리 :14316 kb
import sys
s=list(map(int,sys.stdin.readline().strip().split()))
for i in s:
    print('even' if i%2==0 else 'odd')
