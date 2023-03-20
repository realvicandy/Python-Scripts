"""
Modify the program to use a loop to output a right triangle of height triangle_height. The first line will have one
user-specified character, such as % or *. Each subsequent line will have one additional user-specified character until 
the number in the triangle's base reaches triangle_height. Output a space after each user-specified character, including
a line's last user-specified character.
"""

triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))

# FOR LOOP: use i to loop the range of triangle_height and keep track of the number
# (add 1 extra since i is initialized at 0)
for i in range(triangle_height + 1):
    # OUTPUT the triangle_char multiplied by i with spaces in between each char
    print((triangle_char + ' ') * i)
    # CALCULATE: i is now subtracted by one
    i -= 1

