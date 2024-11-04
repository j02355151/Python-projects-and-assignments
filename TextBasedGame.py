# Hide and Seek Project
# Chun Lau



# a dictionary linking a room to other rooms



rooms= {

    'Living room 1': {'North': 'Kitchen', 'East': 'Living room 2', 'South': 'Master bedroom', 'West': 'Basement'},
    'Kitchen': {'East': 'Dining room', 'West': 'Attic', 'item': 'Lighter'},
    'Attic': {'East': 'Kitchen', 'item': 'fuse'},
    'Dining room': {'West': 'Kitchen', 'item': 'Pocket knife'},
    'Living room 2': {'North': 'Dining room', 'East': 'Guest bedroom 1', 'South': 'Guest bedroom 2', 'item': 'Bloody Bathroom Key'},
    'Guest bedroom 1': {'West': 'Living room 2', 'item': 'Attic key'},
    'Guest bedroom 2': {'North': 'Living room 2', 'item': 'Master Bedroom Key'},
    'Master Bedroom': {'North': 'Living room 1', 'item': 'Basement Key'},
    'Basement': {'East': 'Living room 1', 'West': 'Basement bathroom', 'item': 'watch'},
    'Basement bathroom': {'East': 'Basement', 'item': 'HouseKeeper'} #villain = HouseKeeper
    }
s = ''
    # list for storing player inventory
inventory = []
currentRoom = 'Living room 1'
player_move = ''


#for room in rooms:
    #print("I am in {}".format(room))
    #print(rooms[room])
    #for direction in rooms[room]:
        #print("Moving {} brings me to the {}".format(direction, rooms[room][direction]))

def move(direction, room="Living room 1"):
    print('Why am I here?')
    if direction == 'South':
        #check to see if you can use that direction from the room you are in
        print('I gotta figure out a way out of this house.....')
        return rooms[room]['South']
    if direction == 'North':
        print('I gotta figure out a way out of this house.....')
        return rooms[room]['North']
    if direction == 'East':
        print('You feel a chill down your spine as you enter the room.....')
        return rooms[room]['East']
    if direction == 'West':
        print('Why are all the lights so dim?')
        return rooms[room]['West']
    else:
        print('It is too dark in here, I just ran into a wall.')

def player_stat():
    print()
    print('You are in {}'.format(current_room))
    print('Inventory :'.format(inventory))

def showStatus(currneRoom, inventory, rooms):
    print(currneRoom)
    print(inventory)
    print(rooms)

#show the player the main menu
def show_instructions():
   #print a main menu and the commands
   print('=================================================================')
   print("               Hide and Seek Adventure Game")
   print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
   print("Collect 9 items to win the game, be careful where you explore...")
   print("                 The 9th item is a mystery.")
   print("       Move commands: go South, go North, go East, go West")
   print("              Add to Inventory: get 'item name'")
   print(player_stat())
   print('             type quit if you wish to stop playing')
   print('_________________________________________________________________')

 #define an inventory, which is initally empty
def get_item(currentRoom, move, rooms, inventory):
    # add item to inventory and remove it from the room
    inventory.append(rooms[currentRoom]['item'])
    del rooms[currentRoom]['item']

 #show the player the game instructions
    # loop forever
def move_between_rooms(current_room, move, rooms):
    # move to corresponding room
    current_room = rooms[current_room][move]
    return current_room


def move(direction, room="Living room 1"):
    print('Why am I here?')
    if direction == 'South':
        #check to see if you can use that direction from the room you are in
        print('I gotta figure out a way out of this house.....')
        return rooms[room]['South']
    if direction == 'North':
        print('I gotta figure out a way out of this house.....')
        return rooms[room]['North']
    if direction == 'East':
        print('You feel a chill down your spine as you enter the room.....')
        return rooms[room]['East']
    if direction == 'West':
        print('Why are all the lights so dim?')
        return rooms[room]['West']
    else:
        print('It is too dark in here, I just ran into a wall.')

#Control for program
   # if they type 'go' first

directions = ["North", "South", "East", "West"]

stop = "go"

current_room = "Living room 1"
while stop != 'quit':
    #run the game
    show_instructions()
    user_input = input("What would you like to do?")
    if user_input == 'quit':
        break

    if user_input == 'go South':
        current_room = move('South', current_room)
        print('You have entered the', current_room)
    if user_input == 'go North':
        current_room = move('North', current_room)
        print('You have entered the', current_room)
    if user_input == 'go East':
        current_room = move('East', current_room)
        print('You have entered the', current_room)
    if user_input == 'go West':
        current_room = move('West', current_room)
        print('You have entered the', current_room)
# if invalid move command print error message
while True:
    # Setting the condition for winning/ losing
    if currentRoom == 'Basement bathroom':
        #winning conditions
        if len(inventory) == 8:
            print('You have freed the evil spirit of the HouseKeeper!')
            print('You may now safely walk out of this old and creepy house.')
            print('Thank you for playing!')

        #losing condition
        else:
            print('\nYou Died')
            print('Your Soul is now forever trapped here with the Housekeeper.')
            print('Your first task as a ghost: Clean the bathroom.')
            break

# Tell the user their current room, inventory and prompt for a move, ignores case
        print('You are in the ' + currentRoom)
        print(inventory)
        # tell the user if there is an item in the room
        if current_room != 'Vampires Lair' and 'item' in rooms[currentRoom].keys():
            print('You see the {}'.format(rooms[currentRoom]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        # handle if the user enters a command to move to a new room
        if len(move) >= 2 and move[1] in rooms[currentRoom].keys():
            currentRoom = move_between_rooms(currentRoom, move[1], rooms)
            continue
        # handle if the user enter a command to get an item
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[currentRoom]['item']:
            print('You pick up the {}'.format(rooms[currentRoom]['item']))
            print('------------------------------')
            get_item(currentRoom, move, rooms, inventory)
            continue
        # handle if the user enters an invalid command
        else:
            print('Invalid move, please try again')
            continue

