import sys
from random import randrange
from random import shuffle

def Average(lst):
    return sum(lst) / len(lst)

def print_board():
    for i in range(0,9,3):
        print(board[i],board[i+1],board[i+2])
    print("-------------------------------")

def fill(def_position, def_value):
    board[def_position] = def_value

def check_if_can_fill(def_position, def_value):
    if (board[def_position] == 0 or (board[def_position] != def_value and board[def_position]> 0)):
        return True
    else:
        return False

def check_for_win():
    win = False
    reason = "NOT_WINNER"    
    
    # checking rows equal   
    for i in range(0,9,3):
        # checking rows equal
        if ((board[i] == board[i+1]) and (board[i+1] == board[i+2])) and (board[i] > 0):
            win = True
            reason = "rows equal " + str(i)
            break            
         # checking rows small to big
        if ( ((board[(i)] == 1) and (board[(i+1)] == 2) and (board[(i+2)] == 3)) or ( (board[i] == 3) and (board[(i+1)] == 2)  and (board[(i+2)] == 1)) ):
            win = True
            reason = "rows small to big " + str(i)
            break

    if win:
        print(reason)        
        return win
            
            
    # checking columns equal               
    for i in range(0,3,1):        
         # checking columns equal
        if ((board[i] == board[(i+3)]) and (board[(i+3*1)] == board[(i+3*2)])) and (board[(i)] > 0):
            win = True
            reason = "columns equal " + str(i)
            break
            
         # checking columns small to big
        if (((board[i] == 1) and (board[(i+3*1)] == 2) and (board[(i+3*2)] == 3)) or ((board[i] == 3) and (board[(i+3*1)] == 2) and (board[(i+3*2)] == 1))):
            win = True
            reason = "columns small to big " + str(i)
            break
    if win:
        print(reason)        
        return win
            
    # checking diagonial
    if ( ((board[0] == board[4]) and (board[4] == board[8]) and (board[0] > 0))  or ((board[2] == board[4]) and (board[4] == board[6]) and (board[2] > 0)) ):
        win = True
        if win:
            print("win diagonial equal")   
            return win
    
    # checking diagonial
    if ( (board[4] == 2) and ((board[0] == 1 and board[8] == 3) or (board[0] == 3 and board[8] == 1) or (board[2] == 1 and board[6] == 3) or (board[2] == 3 and board [6] ==1)) ):
        win = True
        if win:
            print("win diagonial small to big")           
            return win
                              
    return win            
        
def play_game():            
    steps = 0
    while circles:
        steps = steps + 1
        circle = circles.pop()
        tmp_pos = randrange(9)
        if check_if_can_fill(tmp_pos,int(circle)):            
            fill(tmp_pos,int(circle))            
            if check_for_win():
                print("Winner at step " + str(steps))
                print_board()
                break                
        else:
            circles.insert(0,circle)          # sos not append
                   
    return steps
    
''' defines a dictionary '''            
'''
{'0': 0 , '1': 0 , '2': 0 ,
 '3': 0 , '4': 0 , '5': 0 ,
 '6': 0 , '7': 0 , '8': 0 }
 '''
board = {0: 0 , 1: 0 , 2: 0 , 3: 0 , 4: 0 , 5: 0 , 6: 0 , 7: 0 , 8: 0 }

small_circles = [1] * 9      # SMALL --> 1 
medium_circles = [2] * 9    # MEDIUM --> 2
big_circles = [3] * 9          # BIG --> 3

steps_to_win = []
for i in range(100):
    #reset here sos
    board = board.fromkeys(board, 0)
    circles = []
    circles = small_circles + medium_circles + big_circles
    shuffle(circles)        
    steps_to_win.append(play_game())
    

print("average number of iteration is " + str(Average(steps_to_win)))