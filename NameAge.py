import datetime

# Getting current year
current_year = datetime.date.today().year

# Get users name
name = input('What is your name?')

# Get users age
age = int(input('What is your age?'))

# Calculate users birth year
birth_year = (current_year - age)

print('Hello {}! You were born in {}.'.format(name, birth_year))
