""" Victor Anderson """
"""
This is an assignment from my IT140 class to create a minigame. This logic will later be used for a bigger project.
Here are some of the instructions for context:
    - Note: For this milestone, you are being given a dictionary and map for a simplified version of the dragon-themed
        game. (They provided the rooms dictionary)
    - Next, you will develop code to meet the required functionality, by prompting the player to enter commands to move between the rooms or exit the game. To achieve this, you must develop the following:
        A gameplay loop that includes:
            - Output that displays the room the player is currently in
            - Decision branching that tells the game how to handle the different commands. The commands can be to either
                move between rooms (such as go North, South, East, or West) or exit.
            - If the player enters a valid “move” command, the game should use the dictionary to move them 
                into the new room.
            - If the player enters “exit,” the game should set their room to a room called “exit.”
            - If the player enters an invalid command, the game should output an error message to the player
                (input validation).
            - A way to end the gameplay loop once the player is in the “exit” room
*** The map of the rooms is shaped like an L. With 'Great hall at the top of the L, 'Bedroom' at the corner of the L
*** and 'Cellar' at the bottom right most ending of the L.
"""

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
