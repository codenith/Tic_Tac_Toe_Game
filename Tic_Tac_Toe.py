import random


# To clear the screen between moves:
def clear_output():
    print("\n"*100)


# Function to display the game board
def display_board(board):
    clear_output()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Testing the display_board
test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)

# Function to take in the player output and also assign their markers as "X" or "O"


def player_input():
    # Setting the marker as an empty string initially
    marker = ' '
    # Keep asking Player 1 to choose X or O
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    # Assign the opposite marker for player 2
    if marker == 'X':
        return ('X', 'O')
    else:
        return('O', 'X')

# testing
# player_input()

# Function that takes in the game board list,a marker(X or 0) and a position (1 to 9) and assigns it to the board


def place_marker(board, marker, position):
    board[position] = marker


# Testing place_marker
# place_marker(test_board, '$', 7)
# display_board(test_board)


# Function that takes in the board and checks whether anyone has won.

def win_check(board, mark):
    return(
        # across the top
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        # across the middle
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        # across the bottom
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        # across the left
        (board[7] == mark and board[4] == mark and board[1] == mark) or
        # across the middle
        (board[8] == mark and board[5] == mark and board[2] == mark) or
        # across the right
        (board[9] == mark and board[6] == mark and board[3] == mark) or
        # across the right diagonal
        (board[9] == mark and board[5] == mark and board[1] == mark) or
        # across the left diagonal
        (board[7] == mark and board[5] == mark and board[3] == mark))

# Testing the win_check function
# win_check(test_board,'X')

# Function to randomly decide which player goes first


def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# Function which returns a boolean value if there is availability of space on the board


def space_check(board, position):
    return board[position] == ' '

# Function which checks whether the board is full and returns a boolean value,True if FULL or False otherwise


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):  # If there any spaces (empty string) left then it will return False
            return False
    return True  # No available spaces and our board is full

# Function  that asks the player's next position  and checks whether if its a free position, then return position for later use


def player_choice(board):
    position = 0  # there is nothing at the index 0 of the board

    # 1st condition: If the position is not in list of possible positions and 2nd condition is when the space is not free
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position(1-9): '))
    return position

# Function which asks the player whether to play again or not and returns a boolean True if wants to play agani


def replay():
    return input('Do you want to play agin? Enter  Yes or No: ').lower().startswith('y')


# Main program
print('Welcome to Tic Tac Toe!')
# while to keep running the game
while True:
    # Set up everything on the board (board,who's first,choose markers X,0)
    theBoard = [' '] * 10
    # Now to set the markers of each players from the function player_input()
    # Player_input()  function return 2 tuple values ,one for each
    player1_marker, player2_marker = player_input()
    # Now to decide whose turn we have to initialise a variable turn with the function choose_first
    turn = choose_first()
    print(turn+' will go first.')

    play_game = input("Are you ready to play? Enter Yes or No: ")
    if play_game.lower().startswith('y'):
        game_on = True
    else:
        game_on = False
    while game_on:
        # Player one's turn
        if turn == 'Player 1':
            display_board(theBoard)  # Displaying the board
            # Position to insert Player 1 marker
            position = player_choice(theBoard)
            # Calling the place_marker function
            place_marker(theBoard, player1_marker, position)
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! Player 1 won the game')
                game_on = False  # Now the game ended ,so comes out of the loop
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

                    # Player 2 turn
        else:
            # Player 2's  turn
            display_board(theBoard)  # Displaying the board
            # Position to insert Player 1 marker
            position = player_choice(theBoard)
            # Calling the place_marker function
            place_marker(theBoard, player2_marker, position)
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! Player 2 won the game')
                game_on = False  # Now the game ended ,so comes out of the loop
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break
