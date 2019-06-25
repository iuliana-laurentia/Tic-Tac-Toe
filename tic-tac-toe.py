board=[["_","_","_"],
       ["_", "_", "_"],
       ["_","_","_"]]

print("Prans was here :P")

def print_board():
    for line in board:
        output=''
        for elem in line:
            output=output+elem+""
        print(output)


def input_data():
        x =input('column number:')
        y= input('row number:')
        return (x,y)


def validation(x, y):

    if not (x.isdigit()==True and y.isdigit()==True):
        return False


    elif int(x)>2 or int(y)>2:
        return False

    elif int(x)<0 or int(y)<0:
        return False

    elif board[int(x)][int(y)]!='_':
        return False

    else:
        return True



def check_winner(player,board):
    for i in [0,1,2]:
       if board[0][i] == board[1][i] == board[2][i] == player:
          return True



    for i in [0,1,2]:
       if board[i][0] == board[i][1] == board[i][2] == player:
          return True


    if board[0][0]==board[1][1]==board[2][2]== player or board[2][0]==board[1][1]==board[0][2]== player:
        return True

    return False


def loop():
    player='x'
    while True:
        print_board()
        print('It is', player,'turn')
        x, y = input_data()
        is_valid =validation(x,y)

        if  is_valid==True:
            board[int(x)][int(y)] = player
            winner_check = check_winner(player, board)
            if winner_check == True:
                print(player, 'is winner')
                return
            if player == 'o':
                player = 'x'
            else:
                player = 'o'
        else:
            print('Please input valid data!')



loop()

