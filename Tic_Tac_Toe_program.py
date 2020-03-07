def main():
	while True:
	    print('Welcome to Tic Tac Toe!')
	    newboard = [' ']*10
	    display_board(newboard)
	    player1_marker, player2_marker = player_input()
	    print(f"Player 1 marker: {player1_marker}")
	    print(f"Player 2 marker: {player2_marker}")
	    
	    turn = choose_first()
	    print(turn + ' will go first')
	    
	    ready_game = input("Ready to play? (Y/N): ").upper()
	    if ready_game == 'Y':
	        start_game = True
	    else:
	        start_game = False
	        
	    while start_game:
	        if turn == 'Player 1':
	            # Show the board
	            display_board(newboard)
	            # Prompt for Player 1 action
	            print("Player1 turn:")
	            # Choose a position
	            position = player_choice(newboard)
	            # Place the marker on the position
	            place_marker(newboard,player1_marker,position)
	            # Check if won
	            if win_check(newboard, player1_marker) == True:
	                display_board(newboard)
	                print("Player1 is the winner!")
	                start_game = False
	            else:
	                if full_board_check(newboard):
	                    display_board(newboard)
	                    print("It's a DRAW!")
	                    break
	                else:
	                    turn = 'Player 2'
	        else:
	            # Show the board
	            display_board(newboard)
	            # Prompt for Player 2 action
	            print("Player2 turn:")
	            # Choose a position
	            position = player_choice(newboard)
	            # Place the marker on the position
	            place_marker(newboard,player2_marker,position)
	            # Check if won
	            if win_check(newboard, player2_marker) == True:
	                display_board(newboard)
	                print("Player2 is the winner!")
	                start_game = False
	            else:
	                if full_board_check(newboard):
	                    display_board(newboard)
	                    print("It's a DRAW!")
	                    break
	                else:
	                    turn = 'Player 1'

	    if not replay():
	        break


from IPython.display import clear_output
def display_board(board):
	# clear_output()
	print('\n'*10)
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input("Player1 pick a marker (X/O): ").upper()
    player1 = marker
    if player1 == 'O':
        player2 = 'X'
    else:
        player2 = 'O'
    
    return (player1, player2)



def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark:
        return True
    elif board[4] == board[5] == board[6] == mark:
        return True
    elif board[7] == board[8] == board[9] == mark:
        return True
    elif board[1] == board[4] == board[7] == mark:
        return True
    elif board[2] == board[5] == board[8] == mark:
        return True
    elif board[3] == board[6] == board[9] == mark:
        return True
    elif board[1] == board[5] == board[9] == mark:
        return True
    elif board[3] == board[5] == board[7] == mark:
        return True
    else:
        return False


import random
def choose_first():
    start = random.randint(1,2)
    
    if start == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    
    for space in range(1,10):
        if space_check(board,space):
            return False
    
    return True   


def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Enter next position (number 1-9): "))
    
    return position


def replay():
    play = ''
    while play.lower() != 'y' and play.lower() != 'n':
        play = input("Do you want to play again?(Y/N) ")
        
    return play.lower() == 'y'



if __name__ == '__main__':
	main()