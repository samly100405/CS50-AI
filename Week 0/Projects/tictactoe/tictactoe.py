"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_x = sum([row.count(X) for row in board])
    num_o = sum([row.count(O) for row in board])
    if num_x == num_o:
        return X
    
    return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    out = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: 
                out.add((i,j))

    return out

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    return board[action[0]][action[1]] == player(board)


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for player in (X, 0):
        # check row
        for row in board:
            if row == [player] * 3:
                return player
            
        # check col
        for col in range(3):
            if [board[row][col] for row in range(3)] == [player] * 3:
                return player

        # check diag
        if [board[i][i] for i in range(3)] == [player] * 3:
            return player
        
        if [board[i][~i] for i in range(3)] == [player] * 3:
            return player

    return None 

def terminal(board):
    return winner(board) != None or all([(EMPTY not in row) for row in board])


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w == O:
        return -1
    
    if w == X:
        return 1
    
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return None
    if (player(board) == X): return max_value(board)[1]
    if (player(board) == O): return min_value(board)[1]


        
        
def max_value(board):
    if terminal(board): return utility(board), None

    v = -math.inf
    best_action = None
    for action in actions(board):
        x = min_value(result(board, action))[0]
        if x > v:
            v = x
            best_action = action
    return v, best_action

def min_value(board):
    if terminal(board): return utility(board), None

    v = math.inf
    best_action = None
    for action in actions(board):
        x = max_value(result(board, action))[0]
        if x < v:
            v = x
            best_action = action
    return v, best_action