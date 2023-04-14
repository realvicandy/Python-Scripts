"""
This is a text based game
All instructions are laid out at the beginning of the game
The map is the file named tbg_map.png
"""


# DISPLAY the goal of the game, move commands, and the initial status update to the user
def show_instructions():
    print("Welcome to the Space Text Adventure Game")
    print()
    print("Instructions: Collect the Sword of Destiny and all five gems to defeat Veldrum and win the game.\n"
          "If you encounter Veldrum before you have collected all of the relics he will surely defeat you!")
    print()
    print("Move commands: go South, go North, go East, go West")
    print()
    print("Add to Inventory: get 'item name'")
    print("-------------------------")
    print("You are on planet Earth.")
    print("Move command(s):\nEast")
    print("Inventory: []")
    print("-------------------------")


# OUTPUT the directions available on the current planet
def valid_direction_commands(planets, planet):
    for k, v in planets[planet].items():
        if k != 'item':
            print(f"go {k}")


# OUTPUT a status update to the user (will be called after every command)
def status_update(planets, planet, current_inventory, directions):
    """Print player's current status"""
    print("-------------------------")
    print(f"You are on planet {planet}.")
    if 'item' in planets[planet] and planets[planet]['item'] not in current_inventory:
        print(f"You see the {planets[planet]['item']}")
    print(f"Inventory: {current_inventory}")
    print("Move command(s): ")
    valid_direction_commands(planets, planet)
    print('-------------------------')


show_instructions()


def main():
    """GAME INFORMATION"""
    # DEFINE dictionary that links all planets and holds all items on specified planets
    planets = {
        'Earth': {'East': 'Zandron'},
        'Zandron': {'North': 'Eldor', 'East': 'Spectical', 'South': 'Laveldrom', 'West': 'Earth', 'item': 'Sword of Destiny'},
        'Eldor': {'East': 'Taumuram', 'South': 'Zandron', 'item': 'Lightening Gem'},
        'Taumuram': {'West': 'Eldor', 'item': 'Fire Gem'},
        'Spectical': {'North': 'Cabin-Z', 'West': 'Zandron', 'item': 'Teleportation Gem'},
        'Cabin-Z': {'South': 'Spectical'},
        'Laveldrom': {'East': 'Branch-52', 'North': 'Zandron', 'item': 'Illusion Gem'},
        'Branch-52': {'West': 'Laveldrom', 'item': 'Power Gem'}
        }
    # INITIALIZE inventory
    inventory = []
    # INITIALIZE current_planet i.e. the starting planet
    current_planet = 'Earth'
    # STORE all valid directions
    valid_directions = ['North', 'South', 'East', 'West']
    # STORE all valid get item commands
    valid_item_commands = [
        'get Sword of Destiny',
        'get Lightening Gem',
        'get Fire Gem',
        'get Illusion Gem',
        'get Power Gem',
        'get Teleportation Gem'
    ]
    """END GAME INFORMATION"""
    """GAME LOGIC"""
    # WHILE the game has not been won
    while len(inventory) != 6 or current_planet != 'Cabin-Z':
        # VALIDATE user input for direction or get item
        while True:
            command = input('Enter your move:\n')
            # CHECK if there's an item on the current_planet
            if 'item' in planets[current_planet]:
                # IF there is, THEN assign that item to planet_item
                planet_item = planets[current_planet]['item']
            else:
                planet_item = ""
            # DEFINE item_command
            item_command = 'get ' + planet_item
            # DEFINE the item that the user is asking for through item command (without the 'get' part)
            specific_user_entered_item = command.replace('get ', '')
            # IF command has any of the valid_directions
            if any(c in command for c in valid_directions):
                for i in planets.keys():
                    if i == current_planet:
                        if any(c in command for c in planets[i]):
                            # THEN change the current_planet to the planet in that direction
                            current_planet = planets[current_planet][command.split()[-1]]
                            break
                        else:
                            print("You can't go that way!")
                break
            # ELSE IF command == item_command:
            elif command == item_command:
                # THEN ADD item to inventory IF item is not in there already
                if planet_item not in inventory:
                    inventory.append(planet_item)
                    print(f'{planet_item} retrieved!')
                    break
                # ELSE IF the item is already in the inventory OUTPUT 'You already have that item'
                elif planet_item in inventory:
                    print('You already have that item!')
                    break
            # ELSE IF the command is to get a valid item but on the wrong planet
            elif any(c in command for c in valid_item_commands) and planet_item != specific_user_entered_item:
                print("Can't get that relic here!")
                break
            # ELSE the input is not valid
            else:
                print('Invalid input, try again.')
                break
        # OUTPUT status update (this will occur after every command)
        status_update(planets, current_planet, inventory, valid_directions)
        # IF you reach Veldrum on Cabin-Z without all 6 relics then you lose!
        if len(inventory) < 6 and current_planet == 'Cabin-Z':
            print('ZAP ZAP Veldrum has destroyed you!')
            break
    # IF you reach Veldrum on Cabin-Z with all 6 relics you defeat him in glorious battle
    if len(inventory) == 6 and current_planet == 'Cabin-Z':
        print("CLASH CLASH CLASH")
        print("Congratulations, you have defeated the mighty Veldrum!!!")
    """END GAME LOGIC"""


main()
print('Game over! Thanks for playing!')
