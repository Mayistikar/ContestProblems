from sys import stdin, stdout

test_cases = int(stdin.readline())
max_count = 0
char_count = 0
max_char = 'a'

for test_case in range(test_cases):
    candies = stdin.readline()
    for char in candies:
        char_count = candies.count(char)
        if char_count > max_count:
            max_count = char_count
            max_char = char
        elif char_count == max_count:
            if max_char > char and ord(char) > 10:
                max_char = char
    stdout.writelines(str(max_count)+" "+max_char+"\n")
    max_count = 0
