"""
Write a program that first reads in the name of an input file and then reads the input file using the file.readlines()
method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show.
Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and
a list of TV shows are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt, separating
multiple TV shows associated with the same key with a semicolon (;). Next, sort the dictionary by values
(alphabetical order), and output the results to a file named output_titles.txt.
"""

storage = {}
input_file = input()

# OPEN and read file
with open(input_file, 'r') as file:
    lines = file.readlines()

# STORE data in a dictionary called storage (number of episodes are keys, show names are values)
for line in range(0, len(lines), 2):
    seasons = int(lines[line].strip())
    show = lines[line + 1].strip()
    if seasons not in storage:
        storage[seasons] = [show]  # STORE string values in lists
    elif seasons in storage:
        storage[seasons].append(show)


# SORT storage by key and write the sorted dict to output_keys.txt
def sort_by_key(directory):
    sorted_key_vals = []
    sorted_keys = sorted(directory.keys())
    for i in sorted_keys:
        titles = "; ".join(directory[i])  # JOIN values together and separate with '; '
        sorted_key_vals.append(f'{i}: {titles}')
    return sorted_key_vals


# SORT storage values and RETURN the sorted values
def sort_by_title(directory):
    sorted_values = []
    for shows in directory.values():
        for s in shows:
            sorted_values.append(s)
    sorted_values.sort()
    return sorted_values


# WRITE the sorted keys with values to the file
with open("output_keys.txt", "w") as new_file:
    for key_val in sort_by_key(storage):
        new_file.write(f'{key_val}\n')

# WRITE the sorted titles to the file
with open("output_titles.txt", "w") as new_file:
    for title in sort_by_title(storage):
        new_file.write(f'{title}\n')
