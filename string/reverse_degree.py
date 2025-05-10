
#https://leetcode.com/problems/reverse-degree-of-a-string/description/


s = "zaza"
alphabets = {}
counter = 26
output = 0

for value in range(97, 123):
    alphabets[chr(value)] = counter
    counter -= 1

for value in range(0, len(s)):
    output += (alphabets[s[value]] * (value + 1))

print(output)


    