import time
import sys

print("""
      
████████╗██╗░█████╗░████████╗░█████╗░░█████╗░████████╗░█████╗░███████╗
╚══██╔══╝██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░██║██║░░╚═╝░░░██║░░░███████║██║░░╚═╝░░░██║░░░██║░░██║█████╗░░
░░░██║░░░██║██║░░██╗░░░██║░░░██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══╝░░
░░░██║░░░██║╚█████╔╝░░░██║░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝███████╗
░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚══════╝
      """)


print("\n")

print("""
    How to win ?    

    Get a sign three times horizontally, vertically or diagonally on the grid, you win!    
      """)

print("Ready to play ?")
x = input("y/n :")
if x == "y":
      print("Start playing")
else:
    sys.exit()

print("\n")


'''mat = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(0)
    mat.append(row)

for m in mat:
    print(m)'''
    
grid = [[0] * 3 for r in range(3)]

grid_symbols = {
    0: '',
    1: 'X',
    2: 'O'
}

def develop_game():
    player_one_turn = True
    while True:
        print_grid()
        player = "Player One" if player_one_turn else "Player Two"
        player_value = 1 if player_one_turn else 2
        
        row, column = get_valid_input(player)
        if grid[row][column] == 0:
            grid[row][column] = player_value
            if check_winner():
                print(f"{grid_symbols[player_value]} WON!")
                print_grid()
                break
            if all(cell != 0 for row in grid for cell in row):
                print("It's a draw!")
                print_grid()
                break
            player_one_turn = switch_player(player_one_turn) # player_one_turn = not player_one_turn # player switch
        else:
            print("Try again with other position.")


  

def switch_player(flag):
    turn_flag = not flag
    return turn_flag

def get_valid_input(player):
    while True:
        row = input(f"{player}, pick a row (1-3): ")
        column = input(f"{player}, pick a column (1-3): ")
        if row.isdigit() and column.isdigit():
            row, column = int(row) - 1, int(column) - 1
            if 0 <= row < 3 and 0 <= column < 3:
                return row, column
        print("Please try a number between 1 and 3.")


def print_grid():
    for index, row in enumerate(grid):
        row_display = " | ".join(grid_symbols[cell] for cell in row)
        print(f"(row) {index + 1} | {row_display}")
    print("    1   2   3  (column)")

def check_winner():
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:  # Row check
            return True
        if grid[0][i] == grid[1][i] == grid[2][i] != 0:  # Column check
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:  # Diagonal check
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:  # Diagonal check
        return True
    return False

develop_game()




