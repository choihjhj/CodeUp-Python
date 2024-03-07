#코드 길이:275 byte(s) / 수행 시간:13 ms / 메모리 :14316 kb
import sys
num = int(sys.stdin.readline().rstrip())

if num < 0:
    if num % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if num % 2 == 0:
        print("C")
    else:
        print("D")
