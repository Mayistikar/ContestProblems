from sys import stdin, stdout
from itertools import imap

test_cases = int(stdin.readline())

for test_case in range(test_cases):
    n, easiest, hardest = imap(str, stdin.readline().split())
    colors = stdin.readline().split()
    if easiest == colors[0] and hardest == colors[-1]:
        stdout.write("BOTH\n")
    elif easiest == colors[0] and hardest != colors[-1]:
        stdout.write("EASY\n")
    elif easiest != colors[0] and hardest == colors[-1]:
        stdout.write("HARD\n")
    else:
        stdout.write("OKAY\n")
