## Create the board
values = [' ' for x in range(1,10)]

###1.Input the choice
def input_a_number (num,position):
    values[position] = num


#2.If the position is free
def vacant_space(position):
    return values[position]== ' '


#print the tic tac toe board
def tic_tac_toe_board(values):
    print("\n")
    print('   |   |   ')
    print(' ' +values[1] + ' | ' + values[2] + ' | ' +values[3])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' +values[4] + ' | ' + values[5] + ' | ' +values[6])
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' +values[7] + ' | ' + values[8] + ' | ' +values[9])
    print('   |   |   ')


#If the position is not free
def check_the_vacant_space(values):
    if values.count(' ') !=0:   #to count the vacant space on the board
        return False
    elif values.count(' ') ==0:
        print("game is over")

#solution = [[1,2,3],[4,5,6][7,8,9],[1,3,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

def winner(values,num):  # all the possible match to win the game that is rows, columns, diagonals.
    return(values[1] ==num and values[2] == num and values[3]== num) or (values[4] == num and values[5] == num and values[6] == num) or (values[7] == num and values[8] == num and values[9] == num) or(values[1] == num and values[4] == num and values[7] == num) or(values[2] == num and values[5] == num and values[8] == num) or(values[3] == num and values[6] == num and values[9] == num) or(values[1] == num and values[5] == num and values[9] == num) or(values[3] == num and values[5] == num and values[7] == num )

#player input logic
def player_move():
    run = True
    while run:
        move = input("Good luck!!! You can choose any number from 1 to 9 according to your choice to insert the X:")
        try:
            move = int(move)
            if move > 0 and move < 10:   #to check if there is place to continue the game.
                if vacant_space(move):
                    run = False
                    input_a_number('X', move)
                else:
                    print('Sorry! the space is already filled!!')
            else:
                print("Input a number from 1 to 9..")
        except:
            print("Oops!! please type a valid number")


def selectRandom(lst):   #lst: all the list created while checking the center value, middle value and edge value.
    import random
    ln = len(lst)
    r = random.randrange(0,ln)     #r is the place chosen by the computer for the current move.
    return lst[r]


#computer play logic
def computer_move():
    possible_move = [i for i, num  in enumerate(values) if num == ' ' and i != 0]
    move = 0
    for n in ['O','X']:
        for x in possible_move:
            valuecopy = values[:]
            valuecopy[x]= n
            if winner(valuecopy, n):
                move = x
                return move

    if 5 in possible_move:                   #center value
        move = 5
        return move

    diagonal_values = []                     #corner values
    for x in possible_move:
        if x in [1,3,7,9]:
            diagonal_values.append(x)
    if len(diagonal_values) >0:
        move = selectRandom(diagonal_values)
        return move

    middle_position = []                     #middle values
    for x in possible_move:
        if x in [2,4,6,8]:
            middle_position.append(x)
    if len(middle_position) >0:
        move = selectRandom(middle_position)
        return move


#main logic
def main():
    print("WELCOME! Let's play TIC TAC TOE.. to play this game you just need to have knowledge of numbers from 1-9 as you dial on smartphone: ")
    tic_tac_toe_board(values)

    while not(check_the_vacant_space(values)):   #to check if the space is not filled you can input your choice
        if not(winner(values, 'O')):             #to check if there is any winner.
            player_move()                        #then it becomes playes turn to play
            tic_tac_toe_board(values)            #To print the board in order to show if the player is won or not
        else:
            print("sorry you lost!")             #If the player won then you lost the game as usual.
            break
        if not(winner(values, 'X')):
            move = computer_move()
            if move == 0:
                print("Sorry! the game is over")
            else:
                input_a_number('O', move)
                print("computer input an O on position of choice", move, ':')    #to show what the computer have chosen at which place
                tic_tac_toe_board(values)


        else:
            print("congrats! you won")
            break

    if check_the_vacant_space(values):
        print("Its a tie")

# Interface
while True:
    y = input("have you ever played a tic tac toe against the machine! now you have just write y and start the game... (y/n):")
    if y=='y':
        values = [' ' for y in range(10)]
        print('************************')
        main()
        y = input("Do you want to play to play again? (y/n):")
        if y=='y':
            values = [' ' for y in range(10)]
            print('************************')
    else:
        print("its over")

