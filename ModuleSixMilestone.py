""" Victor Anderson """

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
        'Great Hall': {'South': 'Bedroom'},
        'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
        'Cellar': {'West': 'Bedroom'}
    }

# INITIALIZE current_room i.e. the starting room
current_room = 'Great Hall'
# STORE all valid directions
directions = ['North', 'South', 'East', 'West', 'exit']
# INITIALIZE the direction string
direction = ''

while direction != "exit":
    """This will continue the game until user enters exit"""
    print(f'You are in the {current_room}.')
    # VALIDATE user input for direction
    while True:
        direction = input('Enter your move:\n')
        if any(d in direction for d in directions):
            break
        else:
            print('Invalid input')
    # LOOP the rooms dictionary
    # IF the direction entered by user is contained in the room THEN navigate to the room of that direction
    for i in rooms.keys():
        if i == current_room:
            if any(d in direction for d in rooms[i]):
                current_room = rooms[current_room][direction.split()[-1]]
                break
            elif direction == 'exit':
                direction = 'exit'
                break
            else:
                print("You can't go that way!")
print('Game over! Thanks for playing!')
