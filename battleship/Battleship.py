
import random
def create_board(size=5):

    board_list = []
    for _ in range(5):
        row = []
        for j in range(5):
            row.append("~")
        board_list.append(row)
    return board_list


# board = [
#     ["~", "~", "~", "~", "~"],
#     ["~", "~", "~", "~", "~"],
#     ["~", "~", "~", "~", "~"],
#     ["~", "~", "~", "~", "~"],
#     ["~", "~", "~", "~", "~"]
# ]

def print_board(board):


    print("  A B C D E")

    for row_num, row in enumerate(board, start=1):
        print(f"{row_num} {" ".join(row)}")




def parse_coordinate(user_input):
    column = ("A", "B", "C", "D", "E")
    letter= user_input[0].upper()
    num = int(user_input[1])

    letter_index = column.index(letter)
    py_index =  num - 1
    return letter_index, py_index



def place_ship(board, ship_length = 3):
    orientation = random.choice(["V", "H"])
    if orientation == "v".upper():
       ship_row = random.randint(0,len(board) - ship_length)
       ship_col = random.randint(0,len(board)-1)

    else:
       ship_row = random.randint(0, len(board)-1)
       ship_col = random.randint(0, len(board) - ship_length)


    for i in range(ship_length):
       if orientation == "V":
           board[ship_row + i][ship_col] = "#"
       else:
            board[ship_row][ship_col+i] = "#"


    return board







board = create_board()
place_ship(board)
turn = 5
while turn >0:

    print_board(board)
    user_choice = input("Enter the your guess: ")
    col, row = parse_coordinate(user_choice)

    if board[row][col] == "#":
        board[row][col] = "X"
        print("HIT")
    elif board[row][col] == "~":
        board[row][col] = "0"
    else:
        print("Already guessed")

    ship_remaining = any("#" in row for row in board)
    if not ship_remaining:
        print("You sank the ship! VICTORY")
        break

    turn -=1













