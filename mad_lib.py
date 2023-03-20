"""
Mad Libs are activities that have a person provide various words, which are then used to complete a short story in
unexpected (and hopefully funny) ways.

Write a program that takes a string and an integer as input, and outputs a sentence using the input values as shown in
the example below. The program repeats until the input string is quit and disregards the integer input that follows.
"""

# INITIALIZE noun with an empty string so that the loop evaluates to true initially
noun = ''

# WHILE LOOP: continue to take inputs until noun is equal to 'quit'
while noun != 'quit':
    # INPUT a noun and number
    noun, num = input().split(" ")
    # IF noun is equal to 'quit' exit loop
    if noun == 'quit':
        break
    # OUTPUT a sentence with noun and number filling in their spots
    print(f'Eating {num} {noun} a day keeps the doctor away.')
