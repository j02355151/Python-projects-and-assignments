def main():

    import turtle
    import time
    import random
    play = True

    WIDTH, HEIGHT = 1000, 1000
    all_players = []
    game_over = False

    # screen
    def init_turtle():
        screen = turtle.Screen()
        screen. setup(WIDTH, HEIGHT)
        screen.title('The Race')

    init_turtle()

    # We want to have 3 players that will answers math questions and if the answer is correct
    # they will move forward toward the finish line
    # First to reach the finish line wins

    # Players settings

    # player 1 - basic set up
    player1 = turtle.Turtle()
    player1.shape('turtle')
    player1.color('green')


    # player 2 - basic set up
    player2 = player1.clone()
    player2.shape('circle')
    player2.color('yellow')


    # player 3 - basic set up
    player3 = player1.clone()
    player3.shape('square')
    player3.color('red')

    # player ref - draws the finish line
    player_ref = player1.clone()
    player_ref.shape('turtle')
    player_ref.color('black')

    #Player position set ups
    player1.penup()
    player1.goto(x= -400, y= 300)
    player2.penup()
    player2.goto(x= -400, y= 0)
    player3.penup()
    player3.goto(x= -400, y= -300)
    player_ref.penup()
    player_ref.goto(x = 400, y= -400)

    # Making a Finish line

    player_ref.left(90)
    player_ref.pendown()
    player_ref.forward(800)
    player_ref.write('     Finish!', font=28)
    player_ref.penup()
    player_ref.forward(400)
    # Creating the random object generator to see who gets to go first




    # Creating the questions to move the turtles forward

    for i in range(30):
        if player1.pos() >= (400, 300):
            print("Player One Wins the Race!")
            break
        if player2.pos() >= (400,0):
            print("Player Two Wins the Race!")
            break
        if player3.pos() >= (400,-300):
            print("Player Three Wins the Race!")
            break

        else:
            num_1 = random.randint(1, 9)
            num_2 = random.randint(1, 9)
            product = num_1 * num_2
            response = int(input(f'Player 1, What is {num_1} * {num_2}? '))
            if response == product:
                player1.forward(250)
                print('Correct! Player will move forward.')
            num_1 = random.randint(1, 9)
            num_2 = random.randint(1, 9)
            product = num_1 * num_2
            response = int(input(f'Player 2, What is {num_1} * {num_2}? '))
            if response == product:
                player2.forward(250)
                print('Correct! Player will move forward.')
            num_1 = random.randint(1, 9)
            num_2 = random.randint(1, 9)
            product = num_1 * num_2
            response = int(input(f'Player 3, What is {num_1} * {num_2}? '))
            if response == product:
                player3.forward(250)
                print('Correct! Player will move forward.')

    # Play again prompt

    restart = input("Do you want to play again?").lower()
    if restart == "yes":
        main()
    else:
        exit()

    #keeps turtle on the screen
    turtle.done

    #finish line

    is_on = True

    while is_on:
        for player in all_players:
            if turtle.xcor() > 330:
                is_on = False

main()