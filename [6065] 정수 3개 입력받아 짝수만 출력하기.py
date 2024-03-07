#코드 길이:106 byte(s) / 수행 시간:10 ms / 메모리 :14316 kb
import sys
s=list(map(int, sys.stdin.readline().rstrip().split()))
for i in s:
    if(i%2==0): print(i)
