from rich.prompt import IntPrompt
from rich.console import Console
from rich.table import Table
from rich.progress import track
from rich import box
from rich import print
from rich.panel import Panel
from rich.text import Text
from random import randrange
from time import sleep

console = Console()
table = Table(title='Game Field', show_header=False, box=box.MINIMAL_DOUBLE_HEAD)
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
count = 1
sign = "X" if count % 2 != 0 else "O"
board[1][1] = "X"


def display_board(board):
    global table
    """The function accepts one parameter containing the board's current status
    and prints it out to the console."""
    for row in board:
        table.add_row(str(row[0]), str(row[1]), str(row[2]), end_section=True)
    console.print(table)
    table = Table(title='Game Field', show_header=False, box=box.MINIMAL_DOUBLE_HEAD)


def enter_move(board):
    """The function accepts the board's current status, asks the user about their move,
    checks the input, and updates the board according to the user's decision."""
    user_move = IntPrompt.ask('Enter your move', choices=[str(el) for el in range(1, 10)])
    if user_move > 9 or user_move < 1:
        console.print('😥Incorrect input.😥', style='bold blue')
        enter_move(board)
    else:
        row = 0 if user_move < 4 else 1 if user_move < 7 else 2
        column = 0 if user_move % 3 == 1 else 1 if user_move % 3 == 2 else 2
        if (row, column) in make_list_of_free_fields(board):
            board[row][column] = 'O'
        else:
            console.print('❌This cell is already filled in.❌', style="bold red")
            enter_move(board)


def make_list_of_free_fields(board):
    """The function browses the board and builds a list of all the free squares;
    the list consists of tuples, while each tuple is a pair of row and column numbers."""
    list = []
    for row in board:
        for col in row:
            if col != "X" and col != 'O':
                list.append((board.index(row), row.index(col)))
    return list


def victory_for(board, sign):
    """The function analyzes the board's status in order to check if
    the player using 'O's or 'X's has won the game"""
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        return False


def draw_move(board):
    """The function draws the computer's move and updates the board."""
    computers_move = randrange(1, 10)
    row = 0 if computers_move < 4 else 1 if computers_move < 7 else 2
    column = 0 if computers_move % 3 == 1 else 1 if computers_move % 3 == 2 else 2
    if (row, column) in make_list_of_free_fields(board):
        board[row][column] = "X"
    else:
        draw_move(board)


def make_progress(type=0):
    for n in track(range(10), description="Processing..."):
        sleep(0.2)


while True:
    if victory_for(board, 'O'):
        make_progress()
        console.print(Panel(Text('🤵You won!🏆', style='green bold', justify="center"), title='Wictory!'))
        break
    elif victory_for(board, "X"):
        make_progress()
        console.print(Panel(Text('🤖Computer won!🤖', style='red bold', justify="center"), title='Wictory!'))
        break
    elif count > 8:
        make_progress()
        console.print(Panel(Text(':bellhop_bell:Draw!:bellhop_bell:', style='yellow', justify="center"), title='Wictory!'))
        break
    try: enter_move(board)
    except KeyboardInterrupt:
        console.print('\nThe game was stoped...', style="green")
        print("Visit my [link=https://github.com/rachkyl]GitHub[/link]!")
    draw_move(board)
    display_board(board)
    count += 1