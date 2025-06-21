# GAME SETUP
valid_markers = ["X", "O"]
valid_columns = [0, 1, 2]

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
game_board = [row1,row2,row3]

winner = False
tie = False
player1_turn = True
player2_turn = False

def player_input():
    row = "start"
    index = "initial"

    row_values = [1, 2, 3]
    index_values = [1, 2, 3]

    row_valid = False
    index_valid = False
        
    while row_valid == False:
        try:
            row = int(input("Select a row (1-3): "))
        except ValueError:
            print("Invalid row input")
            continue

        if row in row_values:
            row_valid = True
        else:
            print("Outside of row values")

    while index_valid == False:
        try:
            index = int(input("Select a column (1-3): "))
        except ValueError:
            print("Invalid index input")
            continue

        if index in index_values:
            index_valid = True
        else:
            print("Outside of index values")
    print()
    return row, index

def place_marker(row_index: tuple, marker: str, board: list):
    row, index = row_index
    marker_placed = False

    while marker_placed == False:
        if board[row-1][index-1] == " ":
            board[row-1][index-1] = marker
            marker_placed = True
        else:
            print("There's already a marker in that space")
            print()
            row, index = player_input()

# WINNING BOARDS
def winning_boards(row1: list, row2: list, row3: list):
    line = ""
    
    # horizontal wins
    if row1[0] == row1[1] == row1[2]:
        line = row1[0] + row1[1] + row1[2]
    elif row2[0] == row2[1] == row2[2]:
        line = row2[0] + row2[1] + row2[2]
    elif row3[0] == row3[1] == row3[2]:
        line = row3[0] + row3[1] + row3[2]

    # vertical wins
    elif row1[0] == row2[0] == row3[0]:
        line = row1[0] + row2[0] + row3[0]
    elif row1[1] == row2[1] == row3[1]:
        line = row1[1] + row2[1] + row3[1]
    elif row1[2] == row2[2] == row3[2]:
        line = row1[2] + row2[2] + row3[2]

    # diagonal wins
    elif row1[0] == row2[1] == row3[2]:
        line = row1[0] + row2[1] + row3[2]
    elif row1[2] == row2[1] == row3[0]:
        line = row1[2] + row2[1] + row3[0]

    return line

def check_tie(board:list):
    marker_count = 0
    for row in board:
        for marker in row:
            if marker in valid_markers:
                marker_count += 1
    return marker_count
        
def check_line(text: str):
    valid_lines = ["XXX", "OOO"]
    if text in valid_lines:
        return True
    else:
        return False

player1 = input("Player 1, please select your marker: 'X' or 'O': ")
while player1.upper() not in valid_markers:
    print("Invalid marker")
    player1 = input("Player 1, please select your marker: 'X' or 'O': ")

player1 = player1.upper()

if player1.upper() == "X":
    player2 = "O"
elif player1.upper() =="O":
    player2 = "X"

while winner == False:

    for row in game_board:
        print(row)
    print()    
    if player1_turn == True:
        print("Player 1's turn")
        place_marker(player_input(), player1, game_board)
        player1_turn, player2_turn = False, True
    elif player2_turn == True:
        print("Player 2's turn")
        place_marker(player_input(), player2, game_board)
        player1_turn, player2_turn = True, False       
    
    winner = check_line(winning_boards(row1, row2, row3))

    if tie == False:
        if check_tie(game_board) == 9:
            tie = True
            break
            
if winner == True:
    if player1_turn == False:
        print("Player 1 wins")
    elif player2_turn == False:
        print("Player 2 wins")
elif tie == True:
    print("Tie game")

for row in game_board:
    print(row)
