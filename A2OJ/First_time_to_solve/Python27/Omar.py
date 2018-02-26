from sys import stdin, stdout
from itertools import imap

test_case = int(stdin.readline())
for i in range(test_case):
    arr = imap(int, stdin.readline().split())
    stdout.write(str(sum(arr)) + '\n')
