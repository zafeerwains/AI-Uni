import math
import random

def end_game():
    restart = input("Do you want to play again? (Yes/No): ")
    if restart.lower() == "yes":
        game(0)
    elif restart.lower() == "no":
        quit()
    else:
        print("Please type Yes or No.")
        end_game()

def build_board(board):
    for x in range(3):
        print(board[x][0], " | ", board[x][1], " | ", board[x][2])
        if x < 2:
            print("-------------")

def check_win(board, is_tie):
    for x in range(3):
        if board[x][0] == board[x][1] == board[x][2] != " " or board[0][x] == board[1][x] == board[2][x] != " ":
            print(board[x][x], "wins!")
            end_game()
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        print(board[1][1], "wins!")
        end_game()
    if is_tie == 9:
        print("It's a tie!")
        end_game()



def player_move(board, is_tie):
    position = input("\nYour Turn\nWhere would you like to go (1-9): ")
    try:
        spot = int(position) - 1
        if board[math.floor(spot / 3)][spot % 3] == " ":
            board[math.floor(spot / 3)][spot % 3] = "X"
        else:
            print("Please choose an empty spot.")
            build_board(board)
            player_move(board, is_tie)
    except ValueError:
        print("Please type a whole number between 1 and 9.")
        build_board(board)
        player_move(board, is_tie)

def game(is_tie):
    board = [[" ", " ", " "] for _ in range(3)]
    build_board(board)
    while True:
        player_move(board, is_tie)
        is_tie += 1
        build_board(board)
        check_win(board, is_tie)
        if is_tie >= 9:
            break
        print("AI's turn:")
        ai_move(board, is_tie)
        is_tie += 1
        build_board(board)
        check_win(board, is_tie)

# Minimax algorithm integration starts here

def minimax(board, depth, is_maximizing):
    if is_game_over(board):
        return get_score(board)

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"  
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "  
                    best_score = max(best_score, score)
        return best_score

    else:
        worst_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"  
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "  
                    worst_score = min(worst_score, score)
        return worst_score

def get_score(board):
    if is_winner(board, "O"):
        return 10
    if is_winner(board, "X"):
        return -10
    return 0

def is_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_game_over(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def ai_move(board, is_tie):
    # Check if there is a winning move for the AI.
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if is_winner(board, "O"):
                    return
                board[i][j] = " "

    # Check if there is a winning move for the player.
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if is_winner(board, "X"):
                    board[i][j] = "O"
                    return
                board[i][j] = " "

    # If there are no winning moves, make a random move.
    while True:
        i = random.randint(0, 2)
        j = random.randint(0, 2)
        if board[i][j] == " ":
            board[i][j] = "O"
            break


# Then call the game function to start the game.
game(0)



