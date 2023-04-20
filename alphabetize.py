"""
This is a script I wrote to alphabetize all the acronyms I am learning while I study for the Security+ exam

It reads the .txt file that I am spamming with acronyms, organizes them alphabetically, then writes the organized
acronyms to a new file

I am writing to a new file because I want to keep the original order of them as well since it goes in order from the
study material
"""

# OPEN the file with the acronyms on it
with open("infosec_acronyms.txt", "r") as file:
    # READ it line by line & alphabetize
    lines = sorted(file.readlines())

# CREATE a new txt file
with open("infosec_acronyms_alphabetical.txt", "w") as new_file:
    # WRITE the organized list to it
    for i in lines:
        new_file.write(i)
