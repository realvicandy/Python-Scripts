# Prompt: Write a program whose inputs are three integers, and whose output is the smallest of the three values.

# Take number inputs
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Store them in my_list
my_list = [num1, num2, num3]

# Sort my_list to ascending order
my_list.sort()

print(my_list[0])