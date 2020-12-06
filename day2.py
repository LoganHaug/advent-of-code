import re

with open("input/day2_input.txt") as input_file:
    passwords = [password.rstrip() for password in input_file]

regex = r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)"
valid_passwords = 0
for password in passwords:
    match = re.match(regex, password)
    if match:
        lower, upper, character, password = int(match[1]), int(match[2]), match[3], match[4]
        occurences = password.count(character)
        if occurences >= lower and occurences <= upper:
            valid_passwords += 1
print(f"Valid Passwords for part 1: {valid_passwords}")

valid_passwords = 0
for password in passwords:
    match = re.match(regex, password)
    if match:
        lower, upper, character, password = int(match[1]), int(match[2]), match[3], match[4]
        if (password[lower-1] == character and password[upper-1] != character):
            valid_passwords += 1
        elif (password[upper-1] == character and password[lower-1] != character):
            valid_passwords += 1
print(f"Valid Passwords for part 2: {valid_passwords}")