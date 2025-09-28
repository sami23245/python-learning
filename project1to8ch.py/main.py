# tic_tac_toe.py
# Fully functional Tic-Tac-Toe with colored X/O and white cell background.
# Requires: colorama (pip install colorama)



from colorama import init, Fore, Back, Style
init(autoreset=True)

def clear_line():
    print()  # simple spacer - console clear not required

# board is a list of 9 elements: ' ' (empty), 'X', or 'O'
def print_board(board):
    """
    Prints the 3x3 board with white cell background and colored X/O.
    Cells are numbered 1..9 for empty display.
    """
    # helper to render a cell with background and colored mark
    def cell_repr(i):
        val = board[i]
        if val == 'X':
            return Back.WHITE + Fore.RED + '  X  ' + Style.RESET_ALL
        elif val == 'O':
            return Back.WHITE + Fore.BLUE + '  O  ' + Style.RESET_ALL
        else:
            # show the cell number for empty cells
            return Back.WHITE + Fore.BLACK + f'  {i+1}  ' + Style.RESET_ALL

    # top border look
    row_sep = Style.DIM + " " + ("+" + "-"*6)*3 + "+" + Style.RESET_ALL
    print(row_sep)
    for r in range(3):
        # print 1 row (3 cells)
        i = r*3
        print(Style.DIM + " " + "|" + Style.RESET_ALL,
              cell_repr(i), Style.DIM + "|" + Style.RESET_ALL,
              cell_repr(i+1), Style.DIM + "|" + Style.RESET_ALL,
              cell_repr(i+2), Style.DIM + "|")
        print(row_sep)

def has_winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a,b,c in wins:
        if board[a] != ' ' and board[a] == board[b] == board[c]:
            return board[a]  # 'X' or 'O'
    return None

def is_full(board):
    return all(cell != ' ' for cell in board)

def ask_move(player, board):
    while True:
        try:
            s = input(f"Player {player} — enter cell number (1-9): ").strip()
            if s.lower() in ('q', 'quit', 'exit'):
                print("Exiting game. Bye!")
                exit(0)
            pos = int(s) - 1
            if pos < 0 or pos > 8:
                print("Choose a number from 1 to 9.")
                continue
            if board[pos] != ' ':
                print("Cell already taken. Choose another.")
                continue
            return pos
        except ValueError:
            print("Please enter a valid number (1-9) or 'q' to quit.")

def play_game():
    board = [' '] * 9
    current = 'X'  # X always starts
    clear_line()
    print(Style.BRIGHT + "Welcome to Colored Tic-Tac-Toe! (type 'q' to quit anytime)\n")
    while True:
        print_board(board)
        move = ask_move(current, board)
        board[move] = current

        winner = has_winner(board)
        if winner:
            print_board(board)
            if winner == 'X':
                print(Fore.RED + Style.BRIGHT + "Player X wins! 🎉")
            else:
                print(Fore.BLUE + Style.BRIGHT + "Player O wins! 🎉")
            break

        if is_full(board):
            print_board(board)
            print(Style.BRIGHT + "It's a tie! (Draw) 🤝")
            break

        # switch player
        current = 'O' if current == 'X' else 'X'

    # ask replay
    while True:
        again = input("Play again? (y/n): ").strip().lower()
        if again in ('y', 'yes'):
            play_game()  # start a new game
            return
        elif again in ('n', 'no'):
            print("Thanks for playing — bye!")
            exit(0)
        else:
            print("Please answer y or n.")

if __name__ == "__main__":
    play_game()

