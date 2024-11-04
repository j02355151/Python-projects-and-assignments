# a dictionary linking a room to other rooms

# show the player the main menu
def main_menu():
    # print a main menu and the commands
    print('=================================================================')
    print("               Hide and Seek Adventure Game")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Collect 9 items to win the game, be careful where you explore...")
    print("                 The 9th item is a mystery.")
    print("       Move commands: go South, go North, go East, go West")
    print("              Add to Inventory: get 'item name'")
    print('             type quit if you wish to stop playing')
    print('_________________________________________________________________')


def move_between_rooms(current_room, move, rooms):
    # move to corresponding room
    current_room = rooms[current_room][move]
    return current_room


# define an inventory, which is empty
def get_item(current_room, move, rooms, inventory):
    # add item to inventory and remove it from the room
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


# show the player the game instructions
# loop forever

def main():
    rooms = {

        'Living room 1': {'North': 'Kitchen', 'East': 'Living room 2', 'South': 'Master bedroom', 'West': 'Basement'},
        'Kitchen': {'East': 'Dining room', 'West': 'Attic','South': 'Living room 1', 'item': 'Used Lighter'},
        'Attic': {'East': 'Kitchen', 'item': 'Old fuse'},
        'Dining room': {'West': 'Kitchen', 'South': 'Living room 2', 'item': 'Flimsy Pocket knife'},
        'Living room 2': {'North': 'Dining room', 'East': 'Guest bedroom 1', 'South': 'Guest bedroom 2','West': 'Living room 1', 'item': 'Bloody Bathroom Key'},
        'Guest bedroom 1': {'West': 'Living room 2', 'item': 'Attic key'},
        'Guest bedroom 2': {'North': 'Living room 2', 'item': 'Master Bedroom Key'},
        'Master Bedroom': {'North': 'Living room 1', 'item': 'Basement Key'},
        'Basement': {'East': 'Living room 1', 'West': 'Basement bathroom', 'item': 'Broken watch'},
        'Basement bathroom': {'East': 'Basement', 'item': 'House Keeper'}  # villain = HouseKeeper
    }
    s = ' '
    # list for storing player inventory
    inventory = []
    current_room = 'Living room 1'
    main_menu()

    # if invalid move command print error message
    while True:
        # Setting the condition for winning/ losing
        if current_room == 'Basement bathroom':
            # winning conditions
            if len(inventory) == 8:
                print('You have freed the evil spirit of the HouseKeeper!')
                print('You may now safely walk out of this old and creepy house.')
                print('Thank you for playing!')
                break
            # losing condition
            else:
                print('\nYou Died')
                print('Your Soul is now forever trapped here with the Housekeeper.')
                print('Your first task as a ghost: Clean the bathroom.')
                break

        # Tell the user their current room, inventory and prompt for a move, ignores case
        print('You are in the ' + current_room)
        print(inventory)
        # tell the user if there is an item in the room
        if current_room != 'Basement bathroom' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        # handle if the user enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # handle if the user enter a command to get an item
        elif len(move[0]) == 3 and move[0] == 'get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            get_item(current_room, move, rooms, inventory)
            continue
        # handle if the user enters an invalid command
        else:
            print('Invalid move, please try again')
            continue


main()
