# Prompt:
# Write a program that takes a date as input and outputs the date's season.
# The input is a string to represent the month and an int to represent the day.

# Spring: March 20 - June 20
# Summer: June 21 - September 21
# Autumn: September 22 - December 20
# Winter: December 21 - March 19

input_month = input()
input_day = int(input())

# Spring
if (input_month == 'March') and (input_day >= 20) and (input_day <= 30):
    print('Spring')
elif (input_month == 'April' or input_month == 'May') and (input_day >= 1) and (input_day <= 30):
    print('Spring')
elif (input_month == 'June') and (input_day >= 1) and (input_day <= 20):
    print('Spring')
# Summer
elif (input_month == 'June') and (input_day >= 21) and (input_day <= 30):
    print('Summer')
elif (input_month == 'July' or input_month == 'August') and (input_day >= 1) and (input_day <= 30):
    print('Summer')
elif (input_month == 'September') and (input_day >= 1) and (input_day <= 21):
    print('Summer')
# Autumn
elif (input_month == 'September') and (input_day >= 22) and (input_day <= 30):
    print('Autumn')
elif (input_month == 'October' or input_month == 'November') and (input_day >= 1) and (input_day <= 30):
    print('Autumn')
elif (input_month == 'December') and (input_day >= 1) and (input_day <= 20):
    print('Autumn')
# Winter
elif (input_month == 'December') and (input_day >= 21) and (input_day <= 30):
    print('Winter')
elif (input_month == 'January' or input_month == 'February') and (input_day >= 1) and (input_day <= 30):
    print('Winter')
elif (input_month == 'March') and (input_day >= 1) and (input_day <= 19):
    print('Winter')
else:
    print('Invalid')
