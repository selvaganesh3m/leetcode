#https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/

from collections import Counter

s = "successes"

vowels = {'a', 'e', 'i', 'o', 'u'}
char_count = Counter(s)
vowel_count = 0
consonant_count = 0

for key, value in char_count.items():
    if key not in vowels:
           consonant_count = max(consonant_count, value)
    else:
          vowel_count = max(vowel_count, value)

print(vowel_count + consonant_count)



