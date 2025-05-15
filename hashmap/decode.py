

#https://leetcode.com/problems/decode-the-message/solutions/2229844/easy-python-solution-using-hashing/

# input 1
# key = "the quick brown fox jumps over the lazy dog"
# message = "vkbs bs t suepuv"

# input 2
key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"

key = key.replace(" ", "")
main_dict = {}
counter = 0
output = ""


for i in range(0, len(key)): #97, 123
    if not main_dict.get(key[i]):
        main_dict[key[i]] = chr(97 + i + counter)
    else:
        counter -= 1

for letter in message:
    if letter == " ":
        output += letter
    else:
        output += main_dict[letter]

print(output)