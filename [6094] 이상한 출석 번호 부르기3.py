#코드 길이:132 byte(s) / 수행 시간:12 ms / 메모리 :14316 kb
import sys
num = int(sys.stdin.readline().rstrip())
numlist = map(int, sys.stdin.readline().rstrip().split())
print(min(numlist))
