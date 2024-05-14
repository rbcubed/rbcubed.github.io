
def initialize_board(m,n):
    A = []
    for i in range(0,m):
        temp = []
        for j in range(0,n):
            temp.append('.')
        A.append(temp)

    return A

def print_board(A):
    """
    A = the game board.
    Size of A = m x n. 6 x 7
    """
    m = len(A)
    n = len(A[0])
    
    tag_line = ' '.join([str(i) for i in range(0,n)])
    print(tag_line)

    board_line = ''

    for i in range(0,m):
        temp_line = ' '.join(A[i][:])
        board_line = board_line + temp_line + '\n'
        
    print(board_line)

def edit_state_of_board(A, c, mark):
    # find which row is assigned to column c here...
    # row is the index of the list A
    m, n = len(A), len(A[0])

    flag_mark = 'unmarked'
    for i in range(m-1,-1,-1):
        if A[i][c] == '.':
            A[i][c] = mark
            flag_mark = 'marked'    
            break

    if flag_mark == 'unmarked':
        print('column already full, select another column')
        
    return A

def check_horizontal(A, i, j, mark):
    m, n = len(A), len(A[0])

    count_h = 1
    
    for h in range(j+1, n):
        if A[i][h] == mark:
            count_h += 1
        else:
            break

    if count_h >= 4:
        win = True
    else:
        win = False

    return win

def check_vertical(A, i, j, mark):
    m, n = len(A), len(A[0])

    count_v = 1
    
    for v in range(i-1, -1,-1):
        if A[v][j] == mark:
            count_v += 1
            #print('count_v: ', count_v, ' for mark: ', mark)
        else:
            break

    if count_v >= 4:
        win = True
        #print('win: ', win)
    else:
        win = False

    return win

def check_left_diag(A, i, j, mark):
    m, n = len(A), len(A[0])

    count_d_left = 1
    if j == 0:
        win = False
    else:
        for d in range(1, m):
            if A[i-d][j-d] == mark:
                count_d_left += 1
                #print('count diag left: ', count_d_left)
            else:
                break
        if count_d_left >= 4:
            win = True
        else:
            win = False

    return win

def check_right_diag(A, i, j, mark):

    m, n = len(A), len(A[0])

    count_d_right = 1
    if j == 6:
        win = False
    else:
        for d in range(1, n-j):
            if A[i-d][j+d] == mark:
                count_d_right += 1
            else:
                break
            
        if count_d_right >= 4:
            win = True
        else:
            win = False
        
    return win

def check_diagonals(A, i, j, mark):

    win_left = check_left_diag(A, i, j, mark)

    if not win_left:
        win_right = check_right_diag(A, i, j, mark)

        if not win_right:
            win = False
        else:
            win = win_right
    else:
        win = win_left

    return win
    

def check_all_directions(A, i, j, mark):
    # horizontal direction
    win_h = check_horizontal(A, i, j, mark)

    if not win_h:
        # vertical direction
        win_v = check_vertical(A, i, j, mark)
        #print('win_v: ', win_v, ' for mark: ', mark)
        if not win_v:
            # diagonals
            win_d = check_diagonals(A, i, j, mark)

            if not win_d:
                win = False
            else:
                win = win_d
        else:
            win = win_v
    else:
        win = win_h

    return win

def check_board_win(A, mark):
    m, n = len(A), len(A[0])

    for i in range(m-1,-1,-1):
        for j in range(0,n):
            if A[i][j] == mark:
                #check in all directions if there are 4 consecutive marks
                #print('checking all...')
                win = check_all_directions(A, i, j, mark)
                #print('check_board_win win: ', win)
                if win == True:
                    return win
    return win

def run_game():
    x = str(input('Player X, enter your name: '))
    o = str(input('Player O, enter your name: '))

    player_dict = {x:'X', o:'O'}
    m, n = 9, 10 

    A = initialize_board(m,n)
    #print(A)

    counter = 0
    while True:
        if counter <= m * n:
            print_board(A)
            
            cx = int(input("{} , you are X. What column do you want to play in?".format(x)))
            A = edit_state_of_board(A, cx, player_dict[x])
            print_board(A)

            game_flag = check_board_win(A, player_dict[x])

            if game_flag:
                print('Player ', x, ' wins!')
                break

            co = int(input("{} , you are O. What column do you want to play in?".format(o)))
            A = edit_state_of_board(A, co, player_dict[o])
            print_board(A)

            game_flag = check_board_win(A, player_dict[o])

            if game_flag:
                print('Player ', o, ' wins!')
                break

            counter += 1
            
            if game_flag:
                break
        else:
            print('No one wins! Try again.')
            break


run_game()
