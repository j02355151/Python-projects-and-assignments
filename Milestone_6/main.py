rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}


def player_stat():
    print("-" * 20)
    print('You are in the {}'.format(currentRoom))
    print("-" * 20)


currentRoom = 'Great Hall'
player_move = ''

while currentRoom != 'Exit':
    player_stat()
    player_move = input('Enter your move:\n').lower()
    if player_move in ['Exit', 'exit']:
        currentRoom = 'Exit'
        print('Play again soon')
        continue

    try:
        currentRoom = rooms[currentRoom][player_move]
    except Exception:
        print("invalid move")
        continue


    if currentRoom == 'Great Hall':
        print("You made it back to the Great Hall")
    elif currentRoom == 'Cellar':
        print('YOU MADE IT TO THE CELLAR, try to go back to the Great Hall')

print("You made it back to the Bedroom")