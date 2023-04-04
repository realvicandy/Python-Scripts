"""
Write a program that gets a list of integers from input, and outputs non-negative integers in ascending
order (lowest to highest).
"""

# GET a list of integers as input from user, store in user_input
user_input = input()

# CONVERT user_input string to integers AND
# IF user_input's current item is >= 0 THEN
# STORE current item in modified_input
modified_input = [int(i) for i in user_input.split() if (int(i) >= 0)]

# sort modified_input in ascending order
modified_input.sort()

# OUTPUT modified_input
for i in modified_input:
    print(i, end=' ')
