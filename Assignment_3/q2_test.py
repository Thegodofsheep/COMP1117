# Begin of your imports ------
import copy
# End of your imports ------

debug = False
# debug = True
# You may uncomment the above line if you want to watch the evoluation of the life, 
# but you MUST comment it when you submit the assignment

def print_game_config(G, generation=-1, debug=True):
    # print for debug, you do not need to modify this function
    if not debug:
        return
    n = len(G)  #len(G) returns the size of G.
    for i in range(n): 
        print(*G[i], sep=', ')
    print(f"End of generation {generation}")

def create_empty_grid(n):
    # Create an empty grid G of size n * n
    # Begin of your implementation ------
    G = [ [0 for j in range(int(n))] for i in range(int(n)) ]
    # End of your implementation ------
    return G

def update_grid_with_input(G, val):
    # Begin of your implementation ------
    coord = []
    while coord != ['-', ' ', '-']:
        coord = list(input())
        if coord == ['-', ' ', '-']:
            return
        G[int(coord[0])][int(coord[2])] = val
    # End of your implementation ------
    return G

def cal_neighbor_mean(x, y, G):
    # Calculate the mean value of neighbors for cell (x, y) in G
    # Begin of your implementation ------
    sum = 0
    neighbors = lambda x, y: [[x2, y2] for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x < n and
                                   -1 < y < n and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 < n) and
                                   (0 <= y2 < n))]
    n_cell_coord = neighbors(x, y)
    sum_list = [G[int(i[0])][int(i[1])] for i in n_cell_coord]
    for j in sum_list:
        sum += j
    mean = sum/len(n_cell_coord)
    # End of your implementation ------
    return mean

def update_game_config(G):
    # Update G to its next generation nextG
    # Begin of your implementation ------
    nextG = copy.deepcopy(G)
    for i in range(0,n):
        for j in range(0,n):
            nextG[i][j] = 5
    # End of your implementation ------
    return nextG 


# Given code - You cannot modify the following code !!!
def input_game_config(n):
    # Input the game config
    G = create_empty_grid(n)
    print("Please input the locations of the angel cells: ")
    update_grid_with_input(G, 20)
    print("Please input the locations of the devil cells: ")
    update_grid_with_input(G, -20)
    return G


if __name__ =='__main__':
    n = int(input("Input the size of the grid: "))
    m = int(input("Input the number of generations: "))

    G = input_game_config(n)
    print_game_config(G, -1, debug=debug)
    for i in range(m):
        G = update_game_config(G)
        print_game_config(G, i, debug=debug)
    print(G)