from sys import stdin, stdout

test_case = int(stdin.readline())
for i in range(test_case):
    arr = [int(x) for x in stdin.readline().split()]
    stdout.write(str(sum(arr)) + '\n')
