"""
Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers
as input, and outputs the average and max.
"""

# GET user inputs, as many as they want to give, store in a list
user_inputs = input().split()
# CONVERT list items from string to integer
for i in range(len(user_inputs)):
    user_inputs[i] = int(user_inputs[i])
# CALCULATE the largest integer of all the inputs, store in a var
max_int = max(user_inputs)
# CALCULATE the average of the inputs, store in a variable
avg = sum(user_inputs) // len(user_inputs)

# OUTPUT the average and max previously calculated
print(avg, max_int)
