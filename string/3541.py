s = "successes"

vowels = "aeiou"
consnants = ""


for i in range(97, 123):
    val = chr(i)
    if val not in vowels:
        consnants += val

char_count = {}

for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

vowel_count = 0
consonant_count = 0

for key, value in char_count.items():
    if key in vowels:
        if vowel_count < char_count[key]:
            vowel_count = char_count[key]
    if key in consnants:
        if consonant_count < char_count[key]:
            consonant_count = char_count[key]

print(vowel_count + consonant_count)



