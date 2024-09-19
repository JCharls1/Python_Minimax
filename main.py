from tkinter import *
import random
import copy
import numpy as np

def next_turn(index):

    global player
    # x:0 o:1
    

    if buttons[index]['text'] == "" and check_winner() is False:

        if player == players[0]:
            buttons[index]['text'] = player
            # curr_board = get_current_board()
            # minimax(curr_board, player)
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif type(check_winner()[0]) == str:
                label.config(text=(players[0]+" wins"))

            elif check_winner()[0] == "Draw":
                label.config(text="Tie!")

        else:
            # perform minimax
            curr_board = get_current_board()
            
            print(curr_board)
            print(minimax(curr_board, player))
            brh = minimax(curr_board, player)
            buttons[int(brh['index'])]['text'] = player            
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif type(check_winner()[0]) == str:
                label.config(text=(players[1]+" wins"))

            elif check_winner()[0] == "Draw":
                label.config(text="Tie!")

def check_winner():
    for h in range(3):
        if buttons[0+3*h]['text'] == 'x' and buttons[1+3*h]['text'] == 'x' and buttons[2+3*h]['text'] == 'x':
            return ["o", 1+3*h, 2+3*h, 3+3*h]
    
    for v in range(3):
        if buttons[0+v]['text'] == 'x' and buttons[3+v]['text'] == 'x' and buttons[6+v]['text'] == 'x':
            return ["x", 1+v, 4+v, 7+v]
    
    if buttons[0]['text'] == 'x' and buttons[4]['text'] == 'x' and buttons[8]['text'] == 'x':
        return ["x", 1, 5, 9]
    elif buttons[2]['text'] == 'x' and buttons[4]['text'] == 'x' and buttons[6]['text'] == 'x':
        return ["x", 3, 5, 7]
    
    for h in range(3):
        if buttons[0+3*h]['text'] == 'o' and buttons[1+3*h]['text'] == 'o' and buttons[2+3*h]['text'] == 'o':
            return ["o", 1+3*h, 2+3*h, 3+3*h]
    
    for v in range(3):
        if buttons[0+v]['text'] == 'o' and buttons[3+v]['text'] == 'o' and buttons[6+v]['text'] == 'o':
            return ["o", 1+v, 4+v, 7+v]
    
    if buttons[0]['text'] == 'o' and buttons[4]['text'] == 'o' and buttons[8]['text'] == 'o':
        return ["o", 1, 5, 9]
    elif buttons[2]['text'] == 'o' and buttons[4]['text'] == 'o' and buttons[6]['text'] == 'o':
        return ["o", 3, 5, 7]
    
    full = True
    for button in buttons:
        if button['text'] == "":
            full = False
    
    if full: return ["Draw", 0,0,0]
    return False

def get_current_board():
    # print(type(buttons))
    curr_board = []
    for n in range(9):
        # print(type(buttons[n]['text']))
        if buttons[n]['text'] == "":
            curr_board.append(str(n))
        else:
            curr_board.append(buttons[n]['text'])
    
    # print(type(curr_board))
    return curr_board

def empty_spaces():

    spaces = 9

    for i in range(9):
        if buttons[i]['text'] != "":
            spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = players[0]

    label.config(text=player + " turn")

    for i in range(9):
        buttons[i].config(text="", bg="#F0F0F0")

def get_available_cells(curr_board):
    result_board = []
    for i in range(9):
        if curr_board[i] == 'x' or curr_board[i] == 'o':
            continue
        else:
            result_board.append(str(i))
    return result_board

def check_winner_two(board, player):
    if ((board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)):
        return True
    else:
        return False

def minimax(board, current_player):
    available_cells = get_available_cells(board)   
    if check_winner_two(board, "x"):
        # print("bruh")
        return {"score": -1}
    elif check_winner_two(board, "o"):
        # print("asda")
        return {"score": 1}
    elif len(available_cells) == 0:
        # print("Asdasd")
        return {"score": 0}
    
    all_info = []
    for i in range(len(available_cells)):
        current_info = {}
        current_info['index'] = board[int(available_cells[i])]
        board[int(available_cells[i])] = current_player
        
        #player[0] human
        if current_player == "o":
            result = minimax(board, "x")
            current_info['score'] = result["score"]
        else:
            result = minimax(board, "o")
            current_info['score'] = result["score"]
        board[int(available_cells[i])] = current_info['index']
        all_info.append(current_info)
    
    best_test_play = 0
    if current_player == "o":
        best_score =  np.iinfo(np.int32).min
        for n in range(len(all_info)):
            if all_info[n]['score'] > best_score:
                best_score = all_info[n]['score']
                best_test_play = n
    else:
        best_score =  np.iinfo(np.int32).max
        for n in range(len(all_info)):
            if all_info[n]['score'] < best_score:
                best_score = all_info[n]['score']
                best_test_play = n
    return all_info[best_test_play]


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = players[0]

buttons = [0] * 9  # Create a 1D list with 9 elements

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()
for i in range(9):
    buttons[i] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                        command=lambda i=i: next_turn(i))
    buttons[i].grid(row=i // 3, column=i % 3)

window.mainloop()
