from sys import stdin, stdout
from itertools import imap

test_cases = int(stdin.readline())
max_kids = 0

for test_case in range(test_cases):
    differ, minim = imap(int, stdin.readline().split())
    max_kids = sum(imap(lambda x: int(x)/minim, stdin.readline().split()))
    stdout.write(str(max_kids)+"\n")
