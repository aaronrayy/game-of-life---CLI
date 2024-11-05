import time
import numpy as np

# creates and returns a dead board state of all 0s
# w -> number of cols, width of board
# h -> number of rows, height/depth of board
def dead_state(w,h):
    cols, rows = (w,h)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    return arr

# creates and returns a board state with randomized 
#       alive (1) and dead (0) cells
# w -> number of cols, width of board
# h -> number of rows, height/depth of board
def random_state(w,h,pr=0.5):
    state = dead_state(w,h)
    state = np.random.choice([0, 1], size=(h, w), p=[1 - pr, pr])
    return state

# Calculates the next board state of a GoL
# INPUT -> initial_state : a 2D array of a GoL board
# RETURNS -> the next board state following the GoL rules
def next_board_state(initial_state):
    rows = len(initial_state)
    cols = len(initial_state[0])
    new_state = dead_state(cols, rows)  # new state array to be returned, initialized to all 0s

    # -> corresponding transformations of current coordinate of the cell 
    #       for each of the 8 neighbors, starting at the top left corner 
    #       and going clockwise
    # -> in an [x,y] pair:
    #       x represents row (i) transformations
    #       y represents column (j) transformations
    shift_arr = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

    # [i][j] is the current cell
    # -> calculate the number of live neighbors that cell in the initial state has
    # -> update that cell to be alive or dead in the new_state board
    for i in range(rows):
        for j in range(cols):
            # calculate number of live neighbors for current cell
            live_neighbors = 0
            for k in range(8):
                if ((i + shift_arr[k][0]) >= 0) and ((j + shift_arr[k][1]) >= 0) and ((i + shift_arr[k][0]) < rows) and ((j + shift_arr[k][1]) < cols):
                    if (initial_state[i + shift_arr[k][0]][j + shift_arr[k][1]]):
                        live_neighbors += 1

            # update cell based on num neighbors
            new_state[i][j] = action(live_neighbors, initial_state[i][j])
    
    return new_state

# Revised version of next_board_state
# CHANGES : Only use shift array on the edges and corners of board.
#           Inner part of board doesnt need neighbor error checking,
#           and therefore can just immediately check for live neighbors
def next_board_state_v2(initial_state):
    rows = len(initial_state)
    cols = len(initial_state[0])
    new_state = dead_state(cols, rows)  # new state array to be returned, initialized to all 0s
    new_state_edges = dead_state(cols, rows)  # new state array to be returned, initialized to all 0s

    # -> corresponding transformations of current coordinate of the cell 
    #       for each of the 8 neighbors, starting at the top left corner 
    #       and going clockwise
    # -> in an [x,y] pair:
    #       x represents row (i) transformations
    #       y represents column (j) transformations
    shift_arr = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]


    # [i][j] is the current cell
    # GOALS:
    #       -> calculate the number of live neighbors that cell in the initial state has
    #       -> update that cell to be alive or dead in the new_state board


    # TOP AND BOTTOM EDGES
    for i in range(0,rows,(rows-1)):
        for j in range(cols):
            # calculate number of live neighbors for current cell
            live_neighbors = 0
            for k in range(8):
                if ((i + shift_arr[k][0]) >= 0) and ((j + shift_arr[k][1]) >= 0) and ((i + shift_arr[k][0]) < rows) and ((j + shift_arr[k][1]) < cols):
                    if (initial_state[i + shift_arr[k][0]][j + shift_arr[k][1]]):
                        live_neighbors += 1

            # update cell based on num neighbors
            new_state_edges[i][j] = action(live_neighbors, initial_state[i][j])

    # LEFT AND RIGHT EDGES
    for i in range(rows):
        for j in range(0,cols,(cols-1)):
            # calculate number of live neighbors for current cell
            live_neighbors = 0
            for k in range(8):
                # using shift array to check neighbors
                if ((i + shift_arr[k][0]) >= 0) and ((j + shift_arr[k][1]) >= 0) and ((i + shift_arr[k][0]) < rows) and ((j + shift_arr[k][1]) < cols):
                    if (initial_state[i + shift_arr[k][0]][j + shift_arr[k][1]]):
                        live_neighbors += 1

            # update cell based on num neighbors
            new_state_edges[i][j] = action(live_neighbors, initial_state[i][j])

    # INNER PART OF GRID
    for i in range(1,(rows-1)):
        for j in range(1,(cols-1)):
            # calculate number of live neighbors for current cell
            live_neighbors = 0
            for k in range(8):
                # error checking not needed since we know these cells all have 8 neighbors
                if (initial_state[i + shift_arr[k][0]][j + shift_arr[k][1]]):
                    live_neighbors += 1

            # update cell based on num neighbors
            new_state[i][j] = action(live_neighbors, initial_state[i][j])

    # MERGE EDGES WITH INNER ARRAY
    return merge_outer_edges(new_state,new_state_edges)

# Merges the outer edges of an array onto another array
# INPUT -> arr1 : array that retains its original inside
#           arr2 : edges of this array are put onto arr1
# RETURNS -> new merged array with inside of arr1 and edges of arr2
def merge_outer_edges(arr1, arr2):
    # Copy arr1 to result so we don't modify the original array
    result = [row[:] for row in arr1]
    
    rows = len(result)
    cols = len(result[0])
    
    # Replace outer edges of arr1 with arr2
    # Replace the first and last rows
    result[0] = arr2[0]  # Top row
    result[-1] = arr2[-1]  # Bottom row
    
    # Replace the first and last elements of the middle rows
    for i in range(1, rows - 1):
        result[i][0] = arr2[i][0]  # Left column
        result[i][-1] = arr2[i][-1]  # Right column
    
    return result


# Returns whether a cell should be alive or dead
#       in standard GoL rule space
# INPUT -> num_neighbors : number of current live neighbors
#       -> alive : bool representing whether current cell is alive or dead
# RETURNS -> 0 for dead, 1 for alive
def action(num_neighbors, alive):
    if alive:
        if (num_neighbors == 2) or (num_neighbors == 3):
            return 1
        else:
            return 0
    else:
        if num_neighbors == 3:
            return 1
        else:
            return 0

def next_board_state_seed(initial_state):
    rows = len(initial_state)
    cols = len(initial_state[0])
    new_state = dead_state(cols, rows)

    # -> corresponding transformations of current coordinate of the cell 
    #       for each of the 8 neighbors, starting at the top left corner 
    #       and going clockwise
    # -> in an [x,y] pair:
    #       x represents row (i) transformations
    #       y represents column (j) transformations
    shift_arr = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

    # [i][j] is the current cell
    # -> calculate the number of live neighbors that cell in the initial state has
    # -> update that cell to be alive or dead in the new_state board
    for i in range(rows):
        for j in range(cols):
            # calculate number of live neighbors for current cell
            live_neighbors = 0
            for k in range(8):
                if ((i + shift_arr[k][0]) >= 0) and ((j + shift_arr[k][1]) >= 0) and ((i + shift_arr[k][0]) < rows) and ((j + shift_arr[k][1]) < cols):
                    if (initial_state[i + shift_arr[k][0]][j + shift_arr[k][1]]):
                        live_neighbors += 1

            # update cell based on num neighbors
            new_state[i][j] = action_seed(live_neighbors, initial_state[i][j])
    
    return new_state

# Returns whether a cell should be alive or dead
#       in seed rule space
# INPUT -> num_neighbors : number of current live neighbors
#       -> alive : bool representing whether current cell is alive or dead
# RETURNS -> 0 for dead, 1 for alive
def action_seed(num_neighbors, alive):
    if alive:
        return 0
    else:
        if num_neighbors == 2:
            return 1
        else:
            return 0
        
# load board state from text file
# INPUT -> text file 
# RETURNS -> initial board state based off text file input
def load_board_state(file_in):
    f = open(file_in)
    arr = []
    for l in f:
        row = []
        for c in l:
            if(c.isalnum()):    # error checking for weird newlines and file formats
                row.append(int(c))
        arr.append(row)
    f.close()
    return arr

# Rendering function to display a running GoL
# INPUT -> state : 2D array of game state
#       -> iter : current generation number
# VARIABLES USED:
    # state[i] -> an entire row i
    # state[i][j] -> the jth element of row i
    # len(state) -> the number of whole rows
    # len(state[0]) -> the number of columns (elements per row) 
def render(state, iter=0):
    rows = len(state)
    cols = len(state[0])

    s = "|"
    for i in range(cols):
        s += ("---")
    s += "|"
    print(s)

    for i in range(rows):
        r = "|"
        for j in range(cols):
            if state[i][j]:
                r += " + "
            else:
                r += "   "
        r += "|"
        print(r)
    print(s)
    print("| Generation: ", iter)

# 1 round of initial board and the next state for testing
def test_one_round(init_s):
    print("initial state:\n")
    render(init_s)
    print("\nnew state:\n")
    render(next_board_state(init_s))

# plays random GoL 
# INPUT -> initial board state
def play_game_soup(init_s):
    curr = init_s
    i = 0
    while(1):
        temp = next_board_state(curr)
        render(temp,i)
        curr = temp
        i += 1
        time.sleep(0.25)

# plays random GoL, with revised next_board_state function
# INPUT -> initial board state
def play_game_soup_v2(init_s):
    curr = init_s
    i = 0
    while(1):
        temp = next_board_state_v2(curr)
        render(temp,i)
        curr = temp
        i += 1
        time.sleep(0.25)

# plays random GoL in the seed rule space
# INPUT -> initial board state
def play_game_seed(init_s):
    curr = init_s
    i = 0
    while(1):
        temp = next_board_state_seed(curr)
        render(temp,i)
        curr = temp
        i += 1
        time.sleep(0.25)

# plays GoL from input text file of starting position
# INPUT -> text file with intitial board state
def play_game_file(file_in):
    curr = load_board_state(file_in)
    i = 0
    while(1):
        temp = next_board_state(curr)
        render(temp,i)
        curr = temp
        i += 1
        time.sleep(0.25)

# plays GoL from input text file of starting position
#       using revised next_board_state function
# INPUT -> text file with intitial board state
def play_game_file_v2(file_in):
    curr = load_board_state(file_in)
    i = 0
    while(1):
        temp = next_board_state_v2(curr)
        render(temp,i)
        curr = temp
        i += 1
        time.sleep(0.25)

# plays game of life from file in the seed rule space
# INPUT -> text file with intitial board state
def play_game_file_seed(file_in,delay=0.25):
    curr = load_board_state(file_in)
    i = 0
    while(1):
        temp = next_board_state_seed(curr)
        render(temp,i)
        curr = temp
        i += 1
        time.sleep(delay)

if __name__ == "__main__":
    #test_one_round()
    init_state = random_state(50,50,0.5)
    #curr = init_state
    #curr = load_board_state("./toad.txt")
    #curr = load_board_state("./beacon.txt")
    #curr = load_board_state("./blinker.txt")
    #curr = load_board_state("./glider.txt")
    curr = load_board_state("./ggg.txt")
    i = 0
    while(1):
        temp = next_board_state_v2(curr)
        render(temp,i)
        curr = temp
        i += 1
        time.sleep(0.25)