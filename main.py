from tkinter import *
import random

def next_turn(index):

    global player

    if buttons[index]['text'] == "" and check_winner() is False:

        if player == players[0]:
            
            buttons[index]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:
            # perform minimax
            buttons[0]['text'] = player            
            minimax(buttons, player)
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    win_conditions = [
        [0, 1, 2],  # first row
        [3, 4, 5],  # second row
        [6, 7, 8],  # third row
        [0, 3, 6],  # first column
        [1, 4, 7],  # second column
        [2, 5, 8],  # third column
        [0, 4, 8],  # first diagonal
        [2, 4, 6],  # second diagonal
    ]

    for condition in win_conditions:
        if buttons[condition[0]]['text'] == buttons[condition[1]]['text'] == buttons[condition[2]]['text'] != "":
            for i in condition:
                buttons[i].config(bg="green")
            return True

    if empty_spaces() is False:
        for i in range(9):
            buttons[i].config(bg="yellow")
        return "Tie"

    return False


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

    player = random.choice(players)

    label.config(text=player + " turn")

    for i in range(9):
        buttons[i].config(text="", bg="#F0F0F0")

def get_available_cells(board):
    result_board = []
    for i in range(9):
        if board[i]['text'] == "x" or board[i]['text'] == "o":
            continue
        else:
            result_board.append(i)

    return result_board

def minimax(board, current_player):
    available_cells = get_available_cells(board)
    print(available_cells)    
    if check_winner():
        return {"score": -1}
    elif not check_winner():
        return {"score": 1}
    else:
        return {"score": 0}
    
    all_info = []
    for i in range(available_cells.size()):
        current_info = {}
        current_info["index"] = board[available_cells[i]]
        board[available_cells[i]] = current_player

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)

buttons = [0] * 9  # Create a 1D list with 9 elements

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()
print(buttons)
for i in range(9):
    buttons[i] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                        command=lambda i=i: next_turn(i))
    buttons[i].grid(row=i // 3, column=i % 3)

window.mainloop()



# from tkinter import *
# import random

# def next_turn(row, column):

#     global player

#     if buttons[row][column]['text'] == "" and check_winner() is False:

#         if player == players[0]:
            
#             buttons[row][column]['text'] = player
#             minimax(buttons)
#             if check_winner() is False:
#                 player = players[1]
#                 label.config(text=(players[1]+" turn"))

#             elif check_winner() is True:
#                 label.config(text=(players[0]+" wins"))

#             elif check_winner() == "Tie":
#                 label.config(text="Tie!")

#         else:
#             # perform minimax
#             buttons[0][0]['text'] = player            
#             minimax(buttons)
#             if check_winner() is False:
#                 player = players[0]
#                 label.config(text=(players[0]+" turn"))

#             elif check_winner() is True:
#                 label.config(text=(players[1]+" wins"))

#             elif check_winner() == "Tie":
#                 label.config(text="Tie!")

# def check_winner():

#     for row in range(3):
#         if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
#             buttons[row][0].config(bg="green")
#             buttons[row][1].config(bg="green")
#             buttons[row][2].config(bg="green")
#             return True

#     for column in range(3):
#         if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
#             buttons[0][column].config(bg="green")
#             buttons[1][column].config(bg="green")
#             buttons[2][column].config(bg="green")
#             return True

#     if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
#         buttons[0][0].config(bg="green")
#         buttons[1][1].config(bg="green")
#         buttons[2][2].config(bg="green")
#         return True

#     elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
#         buttons[0][2].config(bg="green")
#         buttons[1][1].config(bg="green")
#         buttons[2][0].config(bg="green")
#         return True

#     elif empty_spaces() is False:

#         for row in range(3):
#             for column in range(3):
#                 buttons[row][column].config(bg="yellow")
#         return "Tie"

#     else:
#         return False


# def empty_spaces():

#     spaces = 9

#     for row in range(3):
#         for column in range(3):
#             if buttons[row][column]['text'] != "":
#                 spaces -= 1

#     if spaces == 0:
#         return False
#     else:
#         return True

# def new_game():

#     global player

#     player = random.choice(players)

#     label.config(text=player+" turn")

#     for row in range(3):
#         for column in range(3):
#             buttons[row][column].config(text="",bg="#F0F0F0")

# def get_available_cells(board):
#     result_board = []
#     for row in range(3):
#         for column in range(3):
#             if board[row][column]['text'] == "x" or board[row][column]['text'] == "o":
#                 continue
#             else:
#                 result_board.append([row, column])

#     return result_board

# # def minimax(board):
# #     available_cells = get_available_cells(board)
# #     print(available_cells)    
# #     if check_winner():
# #         return {"score": -1}
# #     elif not check_winner():
# #         return {"score": 1}
# #     else:
# #         return {"score": 0}
    
# #     all_info = []
# #     row = 0
# #     col = 0
        
# #     for i in range(available_cells.size() * available_cells[0].size()):
# #         current_info = {}
# #         current_info["index"] = board[row][col]    
        

# window = Tk()
# window.title("Tic-Tac-Toe")
# players = ["x", "o"]
# player = random.choice(players)
# buttons = [[0,0,0],
#            [0,0,0],
#            [0,0,0]]

# label = Label(text=player + " turn", font=('consolas',40))
# label.pack(side="top")

# reset_button = Button(text="restart", font=('consolas',20), command=new_game)
# reset_button.pack(side="top")

# frame = Frame(window)
# frame.pack()

# for row in range(3):
#     for column in range(3):
#         buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
#                                       command= lambda row=row, column=column: next_turn(row,column))
#         buttons[row][column].grid(row=row,column=column)

# # a = {}
# # a["bruh"] = 12
# # a["bruh1"] = 14

# # print(a)

# window.mainloop()