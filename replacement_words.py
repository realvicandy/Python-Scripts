"""
Write a program that replaces words in a sentence. The input begins with word replacement pairs
(original and replacement). The next line of input is the sentence where any word on the original list is replaced.
"""

# GET input strings, STORE every two words in a dictionary original_word as key and replacement_word as value
pairs = {}
user_words = input().split()

original_word = user_words[::2]
replacement_word = user_words[1::2]

for i in range(len(original_word)):
    pairs[original_word[i]] = replacement_word[i]

# GET user input phrase
user_phrase = input()

# # REPLACE substring
for i, j in pairs.items():
    user_phrase = user_phrase.replace(i, j)

# OUTPUT modified user_phrase
print(user_phrase)

