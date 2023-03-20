''' PROMPT: Given a line of text as input, output the number of characters excluding spaces, periods, or commas.'''

user_text = input()
counter = 0

# FOR LOOP: loop the length of user_text
for char in user_text:
    # IF the current char is a whitespace, period, or comma then start loop over with continue
    if char == ' ' or char == '.' or char == ',':
        continue
    # ELSE IF the current char is not a whitespace, period, or comma then increment counter by 1
    else:
        counter += 1
# OUTPUT counter
print(counter)

