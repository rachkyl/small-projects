from random import randrange
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
count = 1
sign = "X" if count % 2 != 0 else "O"


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')
    for row in board:
        print('|       |       |       |')
        print(f'|   {row[0]}   |   {row[1]}   |   {row[2]}   |')
        print('|       |       |       |')
        print('+-------+-------+-------+')


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    user_move = int(input('Enter your move: '))
    if user_move > 9 or user_move < 1:
        print('Incorrect input.')
        enter_move(board)
    else:
        row = 0 if user_move < 4 else 1 if user_move < 7 else 2
        column = 2 if user_move == 9 else (user_move % 3) - 1
        if board[row][column] == 'X' or board[row][column] == 'O':
            print('This cell is already filled in.')
            enter_move(board)
        else:
            board[row][column] = 'O'
            display_board(board)


# def make_list_of_free_fields(board):
#     # The function browses the board and builds a list of all the free squares;
#     # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return False
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return False
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return False
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return False
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return False
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return False
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return False
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return False
    else:
        return True


def draw_move(board):
    # The function draws the computer's move and updates the board.
    computers_move = randrange(1, 10)
    row = 0 if computers_move < 4 else 1 if computers_move < 7 else 2
    column = 2 if computers_move == 9 else (computers_move % 3) - 1
    if board[row][column] == 'X' or board[row][column] == 'O':
        draw_move(board)
    else:
        print("X is playnig:")
        board[row][column] = 'X'
        display_board(board)


board[1][1] = 'X'
while count < 8 and victory_for(board, sign):
    if victory_for(board, 'O'):
        print('You won!')
    elif victory_for(board, "X"):
        print('Computer won.')
    enter_move(board)
    draw_move(board)
    count += 1
