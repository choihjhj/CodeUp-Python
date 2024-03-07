#코드 길이:160 byte(s) / 수행 시간:12 ms / 메모리 :14484 kb
import sys
input=sys.stdin.readline
n=int(input().rstrip())
cnt=[0]*23
s=list(map(int, input().rstrip().split()))
for i in s:
    cnt[i-1]+=1
print(*cnt)
