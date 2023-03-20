'''
Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it
stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

i becomes !
a becomes @
m becomes M
B becomes 8
o becomes .
'''

user_password = input()
modified_password = ''

# FOR LOOP: loop the length of user_password
for char in user_password:
    # IF current char is 'i' then change it to '!'
    if char == 'i':
        modified_password += '!'
        continue
    # ELSE IF current char is 'a' change it to '@'
    elif char == 'a':
        modified_password += '@'
        continue
    # ELSE IF current char is 'm' change it to 'M'
    elif char == 'm':
        modified_password += 'M'
        continue
    # ELSE IF current char is 'B' chage it to '8'
    elif char == 'B':
        modified_password += '8'
        continue
    # ELSE IF current char is 'o' change it to '.'
    elif char == 'o':
        modified_password += '.'
        continue
    # ELSE add current char to the end of modified_password
    else:
        modified_password += char
# OUTPUT
print(modified_password + 'q*s')
