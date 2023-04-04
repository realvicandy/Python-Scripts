"""
Write a program that reads a list of words. Then, the program outputs those words and their frequencies.
"""

# GET user input set of words and split them
user_input = input().split()

# FOR LOOP loops words and prints the word and the count
for word in user_input:
    print(f'{word} {user_input.count(word)}')
