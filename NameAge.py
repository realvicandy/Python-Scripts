import datetime

# This is a simple Python script that takes your name and age and outputs your birth year.
#
# I completed it an assignment for IT140 Intro to Scripting at Southern New Hampshire University
#
# Note: if your birthday for the current year has not yet occured then the output year will be one year greater
#       than it should be. This is how the script had to be written to correctly answer what the prompt was requesting.


# Getting current year
current_year = datetime.date.today().year

# Get users name
name = input('What is your name?')

# Get users age
age = int(input('What is your age?'))

# Calculate users birth year
birth_year = (current_year - age)

print('Hello {}! You were born in {}.'.format(name, birth_year))
