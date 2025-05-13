
#https://leetcode.com/problems/reverse-degree-of-a-string/description/


s = "zaza"
output = 0


for value in range(0, len(s)):
    output += (123 - ord(s[value])) * (value + 1)

print(output)


    